"""
URL configuration for proyectos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    # Redirigir al admin
    
    #paso 1 Redirigir al admin = Cambiar el nombre de la ruta
    #path('admin/', admin.site.urls, name='admin:index'),
    path('admin/', admin.site.urls, name='admin:index'),
    #fin paso 1 Redirigir al admin
    #paso 2 Redirigir al admin = Cambiar el nombre de la ruta
    #return redirect('admin:index')
    #fin paso 2 Redirigir al admin

    path('', views.index, name='index'),
    # paso 1 = LOGIN Crear la ruta en urls.py 
    # path('login/', views.login, name='login'),
    #fin paso 1 LOGIN
    path('Inicio_sesion/', views.login_view, name='Inicio_sesion'),
    path('form_registro/', views.form_registro, name='form_registro'),
    path('profesores/', views.profesores, name='profesores'),
    path('actividades/', views.actividades, name='actividades'),
    path('aprende/', views.aprende, name='aprende'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('form_reg_Profesores/', views.form_reg_Profesores, name='form_reg_Profesores'),
    path('formPrestar/', views.formPrestar, name='formPrestar'),
    path('info/', views.info, name='info'),
    path('nuevo/', views.nuevo, name='nuevo'),
    path('perfil/', views.perfil, name='perfil'),
    path('pruebas/', views.pruebas, name='pruebas'),
]