from django.urls import path
from .views import RegisterView, LoginView, ProfileUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('profile/', ProfileUpdateView.as_view(), name='auth-profile'),
]
