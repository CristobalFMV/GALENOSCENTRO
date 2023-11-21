from django.shortcuts import render, redirect,get_object_or_404
from .models import Usuario
# Create your views here.
def administrador (request):
    usuarioListado = Usuario.objects.all()
    return render (request, "core/administrador.html", {"usuariosLista": usuarioListado})

def home(request):
    return render(request, "core/home.html")

def registrarUsuario(request):
    rut=request.POST['Rut']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    tipodeusuario=request.POST['tipoDeUsuario']
    user = Usuario(rut=rut,nombre=nombre, apellido=apellido,tipodeusuario=tipodeusuario)
    user.save()
    return redirect('/administrador')

def eliminarUsuario(request, rut):
    user=get_object_or_404(Usuario,rut=rut)
    user.delete()
    return redirect('/administrador')

def editarUsuario(request, rut):
    user=get_object_or_404(Usuario,rut=rut)
    return render(request, "core/editUsuario.html" , {"user":user})

def editUsuario(request):
    rut=request.POST['Rut']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    tipodeusuario=request.POST['tipoDeUsuario']
    user=get_object_or_404(Usuario,rut=rut)
    user.nombre = nombre
    user.apellido=apellido
    user.tipodeusuario=tipodeusuario
    user.save()
    return redirect('/administrador')

def calendario(request):
    return render(request,"core/calendario.html")

def secretaria(request):
    return render(request,"core/secretaria.html")

def paciente(request):
    return render(request,"core/paciente.html")


def crearUsuario(request):
    if request.method == 'POST':
        rut = request.POST['Rut']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        # Establece el tipo de usuario predeterminado como "Paciente"
        tipo_de_usuario = 'Paciente'
        
        # Crea el nuevo usuario
        nuevo_usuario = Usuario(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            tipodeusuario=tipo_de_usuario
        )
        nuevo_usuario.save()
        return redirect('/administrador')
    return render(request, 'core/paciente.html')
    