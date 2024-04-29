from .models import Usuario, Mensaje, TipoMensaje
from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse

# Create your views here.
def create_user(data):
    try:
        nuevo_nombre = data.get('nombre')
        nuevo_email = data.get('email')
        
        nuevo_usuario, creado = Usuario.objects.get_or_create(nombre=nuevo_nombre, correo_electronico=nuevo_email)
        return nuevo_usuario, creado
    except IntegrityError:
        raise IntegrityError('Ya existe un usuario con este nombre y correo electrónico')

def create_mensaje(request):
    try:
        if request.method == 'POST':
            data = request.POST
            
            # Crear o obtener el usuario
            nuevo_usuario, creado = create_user(data)
            
            # Obtener o crear el tipo de mensaje
            tipo_mensaje = TipoMensaje.objects.get(tipo=data.get('tipo'))
            
            # Crear el mensaje
            nuevo_mensaje = Mensaje.objects.create(
                usuario=nuevo_usuario,
                tipo=tipo_mensaje,
                asunto=data.get('asunto'),
                contenido=data.get('contenido')
            )
            
            return JsonResponse({'message': 'Mensaje creado correctamente'}, status=201)
            
    except IntegrityError as e:
        return JsonResponse({'error': str(e)}, status=400)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

