from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Inmueble, Perfil
from .forms import UserForm, PerfilForm
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    inmuebles = Inmueble.objects.all()
    context = {
        'inmuebles': inmuebles
    }
    return render(request, 'index.html', context)
    
    
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = UserForm()
#         context = {'form':form}
#         return render(request,'registration/register.html', context)

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            ultimo_usuario_creado = authenticate(request,username=username,password=password)
            login(request,ultimo_usuario_creado)
            
            return HttpResponseRedirect('/profile/')
        context = {'form':form}
        return render(request,'registration/register.html', context)
    else:
        form = UserForm()
        context = {'form':form}
        return render(request,'registration/register.html', context)
        
@login_required(login_url='/login/')
def profile(request):
    usuario = request.user
    perfil = Perfil.objects.filter(usuario=usuario)
    if perfil.exists():
        perfil=perfil[0]
    else:
        perfil = None
        #poder manejar la excepcion
    context = {'perfil':perfil}
    return render(request, 'profile.html',context)
    

@login_required(login_url='/login/')
def register_profile(request):
    usuario = request.user # objeto de tipo User-> auth Django
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            usuario = usuario
            tipo = form.cleaned_data['tipo_usuario']
            rut = form.cleaned_data['rut']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data['telefono']
            correo = usuario.email
            
            datos = Perfil(
                usuario=usuario,
                tipo_usuario=tipo,
                rut=rut,
                direccion=direccion,
                telefono=telefono,
                correo=correo,
                )
            datos.save()
            return HttpResponseRedirect('/profile/')
            
    else:
    #si es que tenemos el metodo get
        form = PerfilForm()
        context = {
            'form':form,
            'title':'Crear perfil'
        }
    return render(request, 'register_profile.html', context)
    

@login_required(login_url='/login/')
def update_profile(request):
    usuario = request.user  
    if request.method == "POST":
        form = PerfilForm(request.POST)
        if form.is_valid():
            perfil = Perfil.objects.filter(usuario=usuario).update(**form.cleaned_data)
            return HttpResponseRedirect('/profile/')
    
    else:

        perfil = Perfil.objects.filter(usuario=usuario)
        if perfil.exists():
            perfil = perfil.first()
            form = PerfilForm(instance=perfil)
            context = {
                'form':form,
                'title':'Actualizar Perfil'
            }
            return render(request, 'register_profile.html', context)
    