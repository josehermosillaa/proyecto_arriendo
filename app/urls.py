from django.urls import path
from .views import (
    index, register, profile,
    register_profile, update_profile,
    register_inmueble, get_inmuebles,
    update_inmueble, contact, messages, delete_inmueble, modal_inmueble, prueba
    )
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/',index, name='home'),
    path('login/', LoginView.as_view(next_page='profile'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('register_profile/', register_profile, name='register_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register_inmueble/<str:username>/', register_inmueble, name='register_inmueble'),
    path('inmuebles/', get_inmuebles, name='get_inmuebles'),
    path('inmueble/<int:pk>/', update_inmueble, name='update_inmueble'),
    path('contact/<int:id>/', contact, name='contact'),
    path('messages/', messages, name='mensaje'),
    path('delete/<int:pk>/', delete_inmueble, name='delete_inmueble'),
    path('modal/<int:pk>/', modal_inmueble, name='modal_inmueble'),
    path('prueba/', prueba, name='prueba'),
    

    

]
