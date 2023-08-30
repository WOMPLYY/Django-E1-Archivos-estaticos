from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Inicio_sesion(request):
    return render(request, 'Inicio_sesion.html')

def form_registro(request):
    return render(request, 'form_registro.html')

def profesores(request):
    return render(request, 'profesores.html')

def actividades(request):
    return render(request, 'actividades.html')

def aprende(request):
    return render(request, 'aprende.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def form_reg_Profesores(request):
    return render(request, 'form_reg_Profesores.html')

def formPrestar(request):
    return render(request, 'formPrestar.html')

def info(request):
    return render(request, 'info.html')

def nuevo(request):
    return render(request, 'nuevo.html')

def perfil(request):
    return render(request, 'perfil.html')

def pruebas(request):
    return render(request, 'pruebas.html')