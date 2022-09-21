from django.urls import path
from .views import QuizView, RandomQuestion, QuizQuestion

app_name = 'quiz'

urlpatterns = [
    path('', QuizView.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='question')
]
