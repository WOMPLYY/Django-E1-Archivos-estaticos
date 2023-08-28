from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def Inicio_sesion(request):
    return render(request, 'Inicio_sesion.html')


def form_registro(request):
    return render(request, 'form_registro.html')

def profesores(request):
    return render(request, 'profesores.html')