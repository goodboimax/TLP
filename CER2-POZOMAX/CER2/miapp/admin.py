from django.contrib import admin
from .models import Entidad, Comunicado
from django.core.exceptions import PermissionDenied

class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo", "entidad", "fecha_publicacion", "fecha_ultima_modificacion", "publicado_por", "modificado_por")
    list_filter = ("fecha_publicacion",)

    def save_model(self, request, obj, form, change):
        if change and (str(obj.entidad) != str(request.user.groups.get())):
            # Si el usuario no es el creador ni pertenece al grupo con la misma entidad denegar la edición
            raise PermissionDenied("No tienes permiso para editar este comunicado.")
        
        elif not change:  # Si está creando un nuevo comunicado
            obj.publicado_por = request.user
        else:
            obj.modificado_por = request.user
        super().save_model(request, obj, form, change)
admin.site.register(Entidad)
admin.site.register(Comunicado)