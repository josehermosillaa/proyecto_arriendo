from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Inmueble
from .forms import UserForm
# Create your views here.
def index(request):
    inmuebles = Inmueble.objects.all()
    context = {
        'inmuebles': inmuebles
    }
    return render(request, 'index.html', context)
    
    
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
        context = {'form':form}
        return render(request,'registration/register.html', context)