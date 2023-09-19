from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm
# from django.contrib.auth.models import User
from users.models import User


def index(request):
    return render(request, 'index.html')

# def Inicio_sesion(request):
#     return render(request, 'Inicio_sesion.html')

# Login

#paso 2 LOGIN = Definir la función login en views.py 
# def login_view(request):
#     return render(request, 'login.html',{
        
#     })
#fin paso 2 LOGIN

# paso 3 LOGIN = En la carpeta templates crear el archivo login.html 
#ir a LOGIN
#fin paso 3 LOGIN

#paso 4 LOGIN = Cambiar la función login en views.py
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         print(username)
#         print(password)

#     return render(request, 'Inicio_sesion.html',{
        
#     })
#fin paso 4 LOGIN

#fin Login

# Autenticación

#paso 1 Autenticación = Agregar librería
    # from django.contrib.auth import login
    # from django.contrib.auth import authenticate
#fin paso 1 Autenticación

#paso 2 Autenticación = Utilizar la función para autenticación 
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             print("Usuario autenticado")
#         else:
#             print("Usuario no autenticado")

#     return render(request, 'Inicio_sesion.html',{
        
#     })
#fin paso 2 Autenticación

# Redirect

#paso 1 Redirect = Agregar librería
# from django.shortcuts import redirect
#fin paso 1 Redirect

#paso 2 Redirect = Función login
#agregar estas 2 librerias al inicio al lado de las demas
# from django.contrib.auth import logout
# from django.contrib import messages
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('index') # Nombre url

#     return render(request, 'Inicio_sesion.html',{
        
#     })
#fin paso 2 Redirect

#paso 3 Redirect = Finalmente, la implementación del login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'Inicio_sesion.html',{

    })
#fin paso 3 Redirect

def logout_view(request):
    logout(request)
    messages.success(request, 'sessión cerrada exitosamente')
    return redirect('Inicio_sesion')

def register(request):
    form = RegisterForm( request.POST or None)

# asi podemos obtener la informacion de un formulario basado en una clase
    if request.method == 'POST' and form.is_valid():

        # username = form.cleaned_data.get('username')
        # email = form.cleaned_data.get('email')
        # password = form.cleaned_data.get('password')

        # print(username)
        # print(email)
        # print(password)


        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('Inicio_sesion')

    return render(request, 'register.html', {
        'form': form
    })
# fin

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