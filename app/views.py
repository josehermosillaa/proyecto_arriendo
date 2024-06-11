from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Inmueble, Perfil, Region, Comuna, Contact
from .forms import UserForm, PerfilForm, InmuebleForm, ContactForm
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    regiones = Region.objects.all()
    comunas = Comuna.objects.all()
    region_id = request.GET.get('region')
    comuna_id = request.GET.get('comuna')
    inmuebles = Inmueble.objects.all()

    if region_id:
        inmuebles = inmuebles.filter(id_region=region_id)
    if comuna_id:
        inmuebles = inmuebles.filter(id_comuna=comuna_id)
    context = {
        'inmuebles': inmuebles,
        'regiones': regiones,
        'comunas': comunas
    }
    return render(request, 'index.html', context)
    
    

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
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

@login_required(login_url='/login/')
def update_inmueble(request, pk):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario.tipo
    inmueble = Inmueble.objects.get(pk=pk)

    if request.method =="POST":
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = Inmueble.objects.filter(pk=pk).update(**form.cleaned_data)
            #el metodo update funciona solo con querysets por lo que no funcionara con el metodo get del object
            
            return HttpResponseRedirect('/inmuebles/')

    ###CON EL GET
    elif inmueble.id_usuario.id == usuario.id:
    #nos traemos el objeto Inmueble con pk = pk
        form = InmuebleForm(instance=inmueble)
        context = {
                    'form':form,
                    'title':'Editar Inmueble',
                    'tipo':tipo
                    }
    else:
        form = 'Inmueble no encontrado'
        context = {
                    'form':form,
                    'title':'Usted no tiene acceso a esta propiedad',
                    'tipo':tipo

                    }
    return render(request,'register_inmueble.html', context)


def contact(request, id):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario.tipo
    inmueble = Inmueble.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['correo']
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            nombre_inmueble = inmueble.nombre_inmueble
            arrendador = inmueble.id_usuario

            data = Contact(
                nombre_inmueble=nombre_inmueble,
                correo=correo,
                arrendador=arrendador,
                nombre=nombre,
                mensaje=mensaje,
            )
            data.save()
            return HttpResponseRedirect('/home/')

    form = ContactForm()
    context = {
                'form':form,
                'title':'Contacta al Propietario',
                'tipo':tipo
            }
    return render(request,'register_inmueble.html', context)
    

def messages(request):
    usuario = request.user
    messages = Contact.objects.filter(arrendador=usuario)
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario.tipo

    context = {
                    'messages':messages,
                    'tipo':tipo
                }
    return render(request, 'contact.html', context)




# @login_required(login_url='/login/')
# def update_profile(request):
#     usuario = request.user  
#     if request.method == "POST":
#         form = PerfilForm(request.POST)
#         if form.is_valid():
#             perfil = Perfil.objects.filter(usuario=usuario).update(**form.cleaned_data)
#             return HttpResponseRedirect('/profile/')
    
#     else:

#         perfil = Perfil.objects.filter(usuario=usuario)
#         if perfil.exists():
#             perfil = perfil.first()
#             form = PerfilForm(instance=perfil)
#             context = {
#                 'form':form,
#                 'title':'Actualizar Perfil'
#             }
#             return render(request, 'register_profile.html', context)

def delete_inmueble(request,pk):
    inmueble = Inmueble.objects.filter(pk=pk)
    inmueble.delete()
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

def modal_inmueble(request, pk):
    usuario = request.user
    tipo = Perfil.objects.get(usuario=usuario).tipo_usuario.tipo
    inmueble = Inmueble.objects.get(pk=pk)
    context = {
            'inmueble':inmueble,
            'tipo': tipo,
            'title':'Registrar Inmueble'
        }
    
    return render(request, 'modal.html', context)

def prueba(request):
    return render(request, 'prueba.html')