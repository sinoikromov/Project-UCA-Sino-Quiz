from .models import Question, Quiz, Answer, Category
from django.views.generic import ListView


class Menu_Quiz(ListView):
    template_name = 'quiz/menu.html'
    queryset = Category.objects.all()
    context_object_name = 'lists'


