from django.urls import path
from .views import indexView, addVehiculo , registroView, loginView, listarVehiculoView, logoutView

urlpatterns = [
    path('', indexView, name = 'index'),
    path('add/', addVehiculo, name = 'index'),
    path('registro/', registroView, name='registro'),
    path('login/', loginView, name='login'),
    path('listar/', listarVehiculoView, name='listar'),
    path('logout/', logoutView, name='logout'),
]