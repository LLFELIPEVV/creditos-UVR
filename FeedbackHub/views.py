from .models import Usuario, Mensaje, TipoMensaje
from django.shortcuts import render
from .forms import MensajeForm
from django.core.mail import send_mail
from django.conf import settings

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
        
        print(f"tipo: {data.get('tipo')}")
        print(f"asunto: {data.get('asunto')}")
        print(f"contenido: {data.get('contenido')}")
        
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
    form = MensajeForm()
    mensaje_aviso = None
    
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = request.POST
            if create_mensaje(mensaje):
                mensaje_aviso = True
            else:
                mensaje_aviso = False
    
    return render(request, 'Comentarios.html', {'form': form, 'mensaje_aviso': mensaje_aviso})
        
        
