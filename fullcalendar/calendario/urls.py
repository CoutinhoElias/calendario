from django.conf.urls import url
import fullcalendar.calendario.views

# Urls para app de calendario
urlpatterns = [
    url(r'^$', fullcalendar.calendario.views.calendario, name='calendario'),
    url(r'^carga_eventos/$', fullcalendar.calendario.views.cargaEventos, name="cargaEventos"),
    url(r'^crea_eventos/$', fullcalendar.calendario.views.creaEventos, name="creaEventos"),
    url(r'^elimina_eventos/$', fullcalendar.calendario.views.eliminaEventos, name="eliminaEventos"),
    url(r'^actualiza_visitador/$', fullcalendar.calendario.views.actualizaVisitador, name="actualizaVisitador"),
    url(r'^api/get_visitadores/$', fullcalendar.calendario.views.get_visitadores, name='get_visitadores'),
    ]
