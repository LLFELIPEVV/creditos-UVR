from .models import Usuario, Mensaje, TipoMensaje
from django.shortcuts import render
from django.db import IntegrityError

# Create your views here.
def create_user(data):
    try:
        nuevo_nombre = data.get('nombre')
        nuevo_email = data.get('email')
        
        nuevo_usuario, creado = Usuario.objects.get_or_create(nombre=nuevo_nombre, correo_electronico=nuevo_email)
        return nuevo_usuario, creado
    except Exception as e:
        return False

def create_mensaje(mensaje):
    try:
        data = mensaje
        
        # Crear o obtener el usuario
        nuevo_usuario, creado = create_user(data)
        
        # Obtener el tipo de mensaje
        tipo_mensaje = TipoMensaje.objects.get(tipo=data.get('tipo'))
        
        # Crear el mensaje
        nuevo_mensaje = Mensaje.objects.create(
            usuario=nuevo_usuario,
            tipo=tipo_mensaje,
            asunto=data.get('asunto'),
            contenido=data.get('contenido')
        )
        
        return True  # Indica que el mensaje se creó correctamente
    
    except Exception as e:
        return False  # Indica que hubo un error al crear el mensaje

def FeedbackHub(request):
    if request.method == 'GET':

        return render(request, 'template_de_Quejas.html')
    elif request.method == 'POST':
        mensaje = request.POST
        if create_mensaje(mensaje):
            mensaje_aviso = 'El mensaje se creó correctamente.'
        else:
            mensaje_aviso = 'Hubo un error al crear el mensaje.'
            
        return render(request, 'template_de_Quejas.html', {'mensaje_aviso': mensaje_aviso})
        
        
