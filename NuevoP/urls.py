"""NuevoP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from NuevoP.views import HelloWorld, segunda_vista, diaDeHoy, miNombreEs, calc_anio_nac, probandoTemplate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hola_Mundo/', HelloWorld),
    path('segundavista/',segunda_vista),
    path('diaDeHoy/',diaDeHoy),
    path('miNombreEs/<nombre>',miNombreEs),
    path('calc_anio_nac/<edad>',calc_anio_nac),
    path('probandotemplate/',probandoTemplate),
]
