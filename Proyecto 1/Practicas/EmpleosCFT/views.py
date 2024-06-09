from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import crear_vacante
from .form import formvacante

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method=='GET':
        return render(request, 'registro.html',{
            'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                usuario.save()
                login(request, usuario)
                return redirect('/publicaciones')
            except IntegrityError:
                return render(request, 'registro.html',{
                'form' : UserCreationForm,
                'error' : 'Nombre de usuario ya existe'
                })
        else:
            return render(request, 'registro.html',{
            'form' : UserCreationForm,
            'error' : 'Contraseñas no coinciden.'
        })

def IniciarSesion(request): 
    if request.method=='GET':
        return render(request, 'inicioSesion.html',{
            'form' : AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if usuario is None:
            return render(request,'login.html',{
            'form' : AuthenticationForm,
            'error': 'Usuario o contraseña incorrecto'
            })
        else:
            login(request, usuario)
            return redirect('/publicaciones')

def publicacion(request):
    practicas = crear_vacante.objects.all()
    return render(request, 'publicaciones.html', {'practicas':practicas})

@login_required
def crear(request):
    if request.method == 'GET':
        return render(request, 'crear_publicacion.html', {'form':formvacante})
    else:
        try:
            vacante = formvacante(request.POST)
            trabajo = vacante.save(commit=False)
            trabajo.empresa = request.user
            trabajo.save()
            return redirect('/publicaciones')
        except ValueError:
            return render(request, 'crear_publicacion.html', {'form':formvacante})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('/')

@login_required
def modificar(request,id_publicacion):
    if request.method == 'GET':
        edicion = get_object_or_404(crear_vacante,pk=id_publicacion,empresa=request.user)
        formulario = formvacante(instance=edicion)
        return render(request,'edicion.html',{'editar':edicion,'datos':formulario})
    else:
        try:
            edicion = get_object_or_404(crear_vacante,pk=id_publicacion,empresa=request.user)
            formulario = formvacante(request.POST,instance=edicion)
            formulario.save()
            return redirect('/publicaciones')
        except ValueError:
            return render(request,'edicion.html',{'editar':edicion,'datos':formulario})

@login_required
def eliminar(request,id_publicacion):
    if request.method == 'POST':
        edicion = get_object_or_404(crear_vacante,pk=id_publicacion,empresa=request.user)
        edicion.delete()
        return redirect('/publicaciones')









