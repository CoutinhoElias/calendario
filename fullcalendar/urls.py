from django.conf.urls import include, url

from django.contrib import admin

from fullcalendar.core.views import index, all_events

admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^all_events/', all_events, name='all_events'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agendamentos/', include('fullcalendar.calendario.urls', namespace='calendario')),
]