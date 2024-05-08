from django.core.management.base import BaseCommand
from FeedbackHub.models import Mensaje

class Command(BaseCommand):
    help = 'Generates a report with the messages'

    def handle(self, *args, **kwargs):
        # Obtener los mensajes de la base de datos
        mensajes = Mensaje.objects.all()

        # Escribir el informe de texto en formato Markdown con una tabla
        reporte = "# Informe de Mensajes\n\n"
        reporte += "| Usuario | Correo electrónico | Tipo | Asunto | Contenido | Fecha | Hora |\n"
        reporte += "| ------- | ------------------- | ---- | ------ | --------- | ----- | ---- |\n"
        for mensaje in mensajes:
            reporte += f"| {mensaje.usuario.nombre} | {mensaje.usuario.correo_electronico} | {mensaje.tipo.tipo} | {mensaje.asunto} | {mensaje.contenido} | {mensaje.fecha} | {mensaje.hora} |\n"

        # Guardar el informe en un archivo de texto con codificación UTF-8
        with open('informe_mensajes.md', 'w', encoding='utf-8') as file:
            file.write(reporte)

        self.stdout.write(self.style.SUCCESS('Informe generado exitosamente en informe_mensajes.md'))
