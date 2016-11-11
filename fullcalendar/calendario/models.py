from django.contrib.auth.models import User
import os
#from PIL import Image

from django.db import models

# Create your models here.

#pip install Pillow
def get_image_path(folder, filename):
    return os.path.join(str(folder), filename)

class UserProfile(models.Model):

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='userprofile')
    #empresa = models.ForeignKey('contabilidad.Empresa', null=True)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=get_image_path, blank=True)
    color = models.CharField(blank=True, max_length=50)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Avaluo(models.Model):
    avaluo_id = models.AutoField(primary_key=True)
    referencia = models.CharField(null=True, max_length=255, unique=False)
    Estatus = models.CharField(null=True, max_length=255)
    Visita = models.DateField(null=True)
    Salida = models.DateField(null=True)
    Solicitud = models.DateField(null=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"


class Evento(models.Model):
    evento_id = models.AutoField(primary_key=True)
    Inicio = models.DateTimeField(null=True, blank=True)
    Fin = models.DateTimeField(null=True, blank=True)
    diaEntero = models.NullBooleanField(null=True, blank=True)
    avaluo = models.ForeignKey(Avaluo, null=True, blank=True)
    asigna = models.ForeignKey("auth.User", null=True, blank=True, related_name='%(class)s_asignacion_created')
    visita = models.ForeignKey("auth.User", limit_choices_to={'groups__name': "Visitadores"}, null=True, blank=True, related_name='%(class)s_visita_created')



