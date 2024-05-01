from django.db import models

# Create your models here.
class TipoMensaje(models.Model):
    tipo = models.CharField(max_length=11, unique=True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=150)
    correo_electronico = models.EmailField(unique=True)
    
    class Meta:
        unique_together = [['nombre', 'correo_electronico']]

class Mensaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoMensaje, on_delete=models.CASCADE)
    asunto = models.CharField(max_length=250)
    contenido = models.TextField()
    fecha = models.DateField(auto_now=True)
    hora = models.TimeField(auto_now=True)
