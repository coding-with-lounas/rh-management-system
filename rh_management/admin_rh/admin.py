from django.contrib import admin
from .models import Employe,Service,Absence,Recrutement,Contrat,Massrouf

# Register your models here.

admin.site.register(Employe)
admin.site.register(Service)
admin.site.register(Absence)
admin.site.register(Recrutement)
admin.site.register(Contrat)
admin.site.register(Massrouf)

