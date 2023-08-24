from django.urls import path, re_path
from .views import RegisterView, LoginView, logout_view, activate, ProfileView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('logout/', logout_view, name='auth-logout'),
    # path('profile/', ProfileUpdateView.as_view(), name='auth-profile'),
    path('activate/<uidb64>/<token>/', views.activate, name='confirm_registration'),
    path('password/', views.change_password, name='change_password'),
    
]
