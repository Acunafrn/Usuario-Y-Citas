from django.contrib import admin
from .models import *
from myapp.models import MyProfile

# Register your models here.
admin.site.register(MyProfile)
admin.site.register(Medico)
admin.site.register(Cita)
admin.site.register(TipoMedico)