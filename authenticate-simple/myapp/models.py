from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class MyProfile(models.Model):
    user = models.OneToOneField(User, 
						on_delete=models.CASCADE, related_name='profile')
    description = models.CharField(max_length=100)


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    """
    Cuando se crea un usuario en Django, esta función se ejecutará
    para crear una instancia de este modelo MyProfile en el campo "usuario".
    """
    if kwargs.get('created', False):
        MyProfile.objects.create(user=kwargs['instance'])

class TipoMedico(models.Model):
    nombre_tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_tipo


class Medico(models.Model):
    nombre_medico = models.CharField(max_length=100)
    tipo_medico = models.ForeignKey(TipoMedico, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre_medico



class Cita(models.Model):
    hora = models.TimeField()
    fecha = models.DateField()
    nombre_medico = models.ForeignKey(Medico, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cita - Fecha: {self.fecha}, Hora: {self.hora}, Médico: {self.nombre_medico}"