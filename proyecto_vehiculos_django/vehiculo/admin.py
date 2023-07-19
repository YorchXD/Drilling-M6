from django.contrib import admin
from .models import VehiculoModel

# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificacion')
    list_filter = ('marca', 'categoria')
    search_fields = ('marca', 'modelo', 'serial_carroceria', 'serial_motor')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    
    #funcion que sustitulle el permiso vehiculo.view_vehiculomodel por vehiculo.vizualizar_catalogo
    def has_view_permission(self, request, obj=None):
        if request.user.has_perm('vehiculo.visualizar_catalogo'):
            return True
        return super().has_view_permission(request, obj)

# Registra el modelo VehiculoModel utilizando la clase VehiculoAdmin
admin.site.register(VehiculoModel, VehiculoAdmin)