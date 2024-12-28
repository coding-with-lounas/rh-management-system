from django.contrib import admin
from .models import Employe,Service,Absence
# Register your models here.

admin.site.register(Employe)
admin.site.register(Service)
admin.site.register(Absence)