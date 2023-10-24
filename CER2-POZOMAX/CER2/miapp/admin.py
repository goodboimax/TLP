from django.contrib import admin
from .models import Entidad, Comunicado
from django.core.exceptions import PermissionDenied


class lista_comunicados(admin.ModelAdmin):
    list_display = ("id","titulo","publicado_por","tipo","fecha_publicacion")
    list_filter = [("publicado_por",admin.RelatedOnlyFieldListFilter),]
    def save_model(self, request, obj, form, change):
        if not change:
            obj.publicado_por = request.user
        super().save_model(request, obj, form, change)



admin.site.register(Entidad)
admin.site.register(Comunicado,lista_comunicados)