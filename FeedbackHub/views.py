from .models import Usuario, Mensaje, TipoMensaje
from django.shortcuts import render
from .forms import MensajeForm

# Create your views here.
def create_user(data):
    try:
        nuevo_nombre = data.get('nombre')
        nuevo_email = data.get('email')
        
        # Verificar si ya existe un usuario con el mismo correo electrónico
        usuario_existente = Usuario.objects.filter(correo_electronico=nuevo_email).first()
        if usuario_existente:
            # Si el usuario ya existe, simplemente lo devuelve
            return usuario_existente, False
        
        # Si no existe, se crea uno nuevo
        nuevo_usuario = Usuario.objects.create(nombre=nuevo_nombre, correo_electronico=nuevo_email)
        return nuevo_usuario, True
    
    except Exception as e:
        print(e)
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
        print(e)
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
        
        
