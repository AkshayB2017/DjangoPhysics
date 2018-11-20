from django.urls import path
from . import views
from . import urls

urlpatterns=[
    path('',views.index,name='index'),
    path('kinematics/', views.kinematics, name="kinematics"),
    path('dynamics/', views.dynamics, name="dynamics"),
    path('thermodynamics/', views.thermodynamics, name="thermodynamics"),
    path('electronics/', views.electronics, name="electronics")
]    