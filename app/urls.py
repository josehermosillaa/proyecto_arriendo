from django.urls import path
from .views import index, register, profile, register_profile, update_profile
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',index, name='home'),
    path('login/', LoginView.as_view(next_page='profile'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('register_profile/', register_profile, name='register_profile'),
    path('update_profile/', update_profile, name='update_profile'),

]
