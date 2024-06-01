from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Inmueble
from .forms import UserForm,PerfilForm
from django.contrib.auth.models import User 
from django.contrib.auth import login,authenticate
# Create your views here.
def index(request):
    inmuebles = Inmueble.objects.all()
    context = {
        'inmuebles': inmuebles
    }
    return render(request, 'index.html', context)
    
    
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
            return HttpResponseRedirect('/')
        context = {'form':form}
        return render(request,'registration/register.html', context)
    else:
        form = UserForm()
        context = {'form':form}
        return render(request,'registration/register.html', context)

        