import json as simplejson
import datetime

from fullcalendar.calendario.models import Evento, Avaluo
#from app.models import Avaluo, UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.utils.encoding import smart_str


def get_visitadores(request):
    if request.is_ajax():
        visitadores = User.objects.filter(groups__name='Visitadores')
        results = []
        for visitador in visitadores:
            visitador_json = {}
            visitador_json['label'] = visitador.first_name
            visitador_json['value'] = visitador.id
            results.append(visitador_json)
        data = simplejson.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def calendario(request):
    avaluos = Avaluo.objects.filter(Estatus__contains='PROCESO', Visita__isnull=True, Salida__isnull=True) | Avaluo.objects.filter(Estatus__contains='DETENIDO', Visita__isnull=True, Salida__isnull=True)
    avaluos = avaluos.order_by('-Solicitud').exclude(avaluo_id__in = Evento.objects.all().values_list('avaluo_id', flat=True))
    #return render_to_response('calendario/extra-calendar-2.html', {'avaluos': avaluos}, context_instance=RequestContext(request))
    return render(request, 'calendario/extra-calendar-2.html', avaluos)


@csrf_exempt
def creaEventos(request):

    event = {}

    title = request.POST.get("title", "")
    if (title is not None and title != ''):
        event['title'] = title[0:(title.index('-')-1)]
    else:
        event['title'] = ""

    # allDay is received from the POST object as a string - change to boolean
    allDay_str = request.POST.get("allDay", "")
    if(allDay_str == "true"):
        event['allDay'] = True
    else:
        event['allDay'] = False

    start = request.POST.get("start", "")
    start = int(start)/1000

    start = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')

    event['start'] = start

    # Set end-date if it exists
    end = request.POST.get("end", "")
    if (end is not None and end != ''):
        end = request.POST.get("end", "")
        end = int(end)/1000
        end = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')
        event['end'] = end
    else:
        event['end'] = event['start']

    avaluo_id = request.POST.get("avaluo_id", "")
    if (avaluo_id is not None and avaluo_id != ''):
        event['avaluo_id'] = request.POST.get("avaluo_id", "")

    # Set entry colour if it exists
    color = request.POST.get("color", "")
    if (color is not None and color != ''):
        event['color'] = request.POST.get("color", "")

    # Return the ID of the added (or updated) calendar entry
    output = {}
    # Add or update collection record, determined by whether it has an ID or not
    record_id = request.POST.get("id", "")
    if(record_id is not None and record_id != ''):
        event_id = Evento.objects.filter(evento_id=record_id)
        event_id.update(Inicio=event['start'], Fin=event['end'], diaEntero=event['allDay'], asigna_id=request.user.id)
        output['id'] = record_id
    else:
        avaluo = 'Título inserido na view createEventos linha 90'#Avaluo.objects.get(FolioK=event['title'])
        insert_id = Evento(None, event['start'], event['end'], event['allDay'], avaluo.avaluo_id, request.user.id, '')
        insert_id.save()
        obj = Evento.objects.latest('evento_id')
        output['id'] = obj.evento_id

    # Output in JSON
    outputStr = simplejson.dumps(output)
    return HttpResponse(outputStr)


@csrf_exempt
def cargaEventos(request):
    start = request.POST.get("start", "")
    end = request.POST.get("end", "")
    eventos = Evento.objects.filter(Inicio__gte=start, Fin__lte=end)

    data = {}
    eventos_json = []
    for e in eventos:
        data['id'] = int(e.evento_id)
        data['title'] = str(e.avaluo.FolioK) + " - " + smart_str(e.avaluo.Colonia)
        data['start'] = e.Inicio.strftime("%Y-%m-%dT%H:%M:%S")
        data['end'] = e.Fin.strftime("%Y-%m-%dT%H:%M:%S")
        data['allDay'] = e.diaEntero
        if e.visita:
            data['visitador'] = e.visita.id
            user_prof = 1 #UserProfile.objects.filter(user_id=e.visita.id).first()
            if user_prof:
                data['color'] = user_prof.color
        eventos_json.append(data)
        data = {}
    return HttpResponse(simplejson.dumps(eventos_json))


@csrf_exempt
def eliminaEventos(request):
    output = {}
    record_id = request.POST.get("id", "")
    if(record_id is not None and record_id != ''):
        event_id = Evento.objects.get(evento_id=record_id)
        event_id.delete()
        output['id'] = record_id
    return HttpResponse(record_id)


@csrf_exempt
def actualizaVisitador(request):
    output = {}
    record_id = request.POST.get("id", "")
    visitador_id = request.POST.get("visitador_id", "")
    if(record_id is not None and record_id != ''):
        event_id = Evento.objects.filter(evento_id=record_id)
        event_id.update(visita=visitador_id)

        output['id'] = record_id
    return HttpResponse(record_id)
