"""WolframPhysics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('calculate/', include('calculate.urls')),
    path('Motion3rdLaw/',include('Motion3rdLaw.urls')),
    path('equation/',include('equation.urls')),
    path('force/',include('force.urls')),
    path('power/',include('power.urls')),
    path('work/',include('work.urls')),
    path('potential/',include('potential.urls')),
    path('powerv/',include('powerv.urls')),
    path('pressuret/',include('pressuret.urls')),
    path('voltage/',include('voltage.urls')),
    path('resistance/',include('resistance.urls')),
    path('gravg/',include('gravg.urls')),
    path('gravforce/',include('gravforce.urls')),
    path('current/',include('current.urls')),
    path('escapev/',include('escapev.urls')),
    path('kinetic/',include('kinetic.urls')),
    path('kinetict/',include('kinetict.urls')),
]

urlpatterns += staticfiles_urlpatterns()
