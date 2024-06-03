from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Inmueble, Perfil
from .forms import UserForm, PerfilForm, InmuebleForm
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
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario.tipo

    perfil = Perfil.objects.filter(usuario=usuario)
    if perfil.exists():
        perfil=perfil[0]
    else:
        perfil = None
        #poder manejar la excepcion
    context = {
        'perfil':perfil,
        'tipo':tipo
        }
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

@login_required(login_url='/login/')
def register_inmueble(request, username):
    #usuario = User.objects.get(username=username)
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario.tipo
    if request.method == "POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            usuario = usuario
            tipo_inmueble = form.cleaned_data['id_tipo_inmueble']
            comuna = form.cleaned_data['id_comuna']
            region = form.cleaned_data['id_region']
            nombre_inmueble = form.cleaned_data['nombre_inmueble']
            m2_construido = form.cleaned_data['m2_construido']
            numero_banos = form.cleaned_data['numero_banos']
            numero_hab = form.cleaned_data['numero_hab']
            direccion = form.cleaned_data['direccion']
            descripcion = form.cleaned_data['descripcion']
            
            datos = Inmueble(
                id_usuario=usuario,
                id_tipo_inmueble=tipo_inmueble,
                id_comuna=comuna,
                id_region=region,
                nombre_inmueble=nombre_inmueble,
                m2_construido=m2_construido, 
                numero_banos=numero_banos,
                numero_hab=numero_hab,
                direccion=direccion,
                descripcion=descripcion
            )
            datos.save()
            return HttpResponseRedirect('/inmuebles/')
    else:
        form = InmuebleForm()
        context = {
                'form':form,
                'tipo':tipo,
                'title':'Registrar Inmueble'
            }
        return render(request, 'register_inmueble.html', context)

    

@login_required(login_url='/login/')
def get_inmuebles(request):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario.tipo
    # usuario = User.objects.get(username=username)
    inmuebles = Inmueble.objects.filter(id_usuario=usuario)
    context = {
            'inmuebles':inmuebles,
            'tipo': tipo,
            'title':'Registrar Inmueble'
        }
    return render(request, 'inmuebles.html', context)
