from django.db import models
from django.conf import settings

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    class Meta:
        verbose_name = "Entidad"
        verbose_name_plural = "Entidades"

    def __str__(self) -> str:
        return self.nombre

class Comunicado(models.Model):
    TIPO_CHOICES = [("S","Suspencion de actividades"),
                    ("C","Suspencion de clase"),
                    ("I","Informacion")]
    id = models.BigAutoField(primary_key =True)
    titulo = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    detalle_corto = models.CharField(max_length=50)
    Entidad = models.ForeignKey("Entidad", on_delete=models.CASCADE,null=True)
    tipo = models.TextField(max_length=1,choices=TIPO_CHOICES)
    visible = models.BooleanField()
    fecha_publicacion = models.DateTimeField(auto_now=False, auto_now_add=False)
    fecha_ultima_publicacion = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    publicado_por  = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="publicado_por",on_delete=models.CASCADE, null=True,editable=False)
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="modificado_por", on_delete=models.CASCADE, editable=False, null=True)
    
    def __str__(self) -> str:
        return self.titulo
    