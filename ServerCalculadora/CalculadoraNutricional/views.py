from django.shortcuts import render
from .models import Usuario

# Create your views here.

def index(request):
    return render(request, 'CalculadoraNutricional/index.html')

def usuarios(request):
    usuario = Usuario.objects.all()
    return render(request, 'CalculadoraNutricional/usuarios.html',{'data': usuario})