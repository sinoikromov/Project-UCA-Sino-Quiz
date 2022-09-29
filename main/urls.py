from .views import home, register
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('accounts/register', register, name='register')
]
