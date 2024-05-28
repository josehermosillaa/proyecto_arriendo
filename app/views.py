from django.shortcuts import render, HttpResponse
from .models import Inmueble
# Create your views here.
def index(request):
    inmuebles = Inmueble.objects.all()
    context = {
        'inmuebles': inmuebles
    }
    return render(request, 'index.html', context)