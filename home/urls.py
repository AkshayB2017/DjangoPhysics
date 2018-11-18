from django.urls import path
from . import views
from . import urls

urlpatterns=[
    path('',views.index,name='index')
]