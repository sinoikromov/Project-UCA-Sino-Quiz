from django.urls import path
from .views import Menu_Quiz

app_name = 'quiz'

urlpatterns = [
   path('', Menu_Quiz.as_view(), name='main_quiz'),
]
