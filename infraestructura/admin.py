from django.contrib import admin
from .models import *

class LineaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_linea": ("descripcion",)}

class CelulaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_celula": ("nombre",)}

admin.site.register(Linea, LineaAdmin)
admin.site.register(Celula, CelulaAdmin)
admin.site.register(RedLan)
# Register your models here.
