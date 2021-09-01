"""encuesta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib      import admin
from django.urls         import path, include   # Nota: para iniciar una nueva aplicacion tengo que usar el comando: 
                                                # django-admin startapp y el nombre de la app sin comillas

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name= 'irinicio'), # Esta url se encuntra en la carpeta de encustas 'principal' 
                                              # que ahi es donde van todas las configuraciones del proyecto
                                              # y esta url esta redirigida a la carpeta templantes donde esta el archivo inicio.html 

    path('Usuarios/', include('apps.usuarios.urls')), # Usuarios url de la aplicacion... 

    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),

    path('logout/', auth_views.logout_then_login, name="logout") # Esto ultimos dos tienen al parecer sus propias views importadas 
                                                                    # de otras clase o nose como decirlo bien... tengo que seguir.
]
