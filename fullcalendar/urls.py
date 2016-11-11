from django.conf.urls import include, url

from django.contrib import admin

from fullcalendar import calendario
from fullcalendar.calendario import views
from fullcalendar.core.views import index, all_events

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^all_events/', all_events, name='all_events'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^agendamentos/', include('fullcalendar.calendario.urls', namespace='calendario')),

    url(r'^calendario/$', views.calendario, name='calendario'),
    url(r'^carga_eventos/$', views.cargaEventos, name="cargaEventos"),
    url(r'^crea_eventos/$', views.creaEventos, name="creaEventos"),
    url(r'^elimina_eventos/$', views.eliminaEventos, name="eliminaEventos"),
    url(r'^actualiza_visitador/$', views.actualizaVisitador, name="actualizaVisitador"),
    url(r'^api/get_visitadores/$', views.get_visitadores, name='get_visitadores'),
]