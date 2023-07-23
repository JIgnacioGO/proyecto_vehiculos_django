from django.urls import path
from . import views

app_name = 'vehiculo'

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add', views.vehiculo_add, name='vehiculo_add'),
    path('list/', views.vehiculo_list, name='vehiculo_list'),
    path('signup/', views.signup, name='signup'),

]
