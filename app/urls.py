from django.urls import path
from .views import index, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',index, name='home'),
    path('login/', LoginView.as_view(next_page='home'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register')

]
