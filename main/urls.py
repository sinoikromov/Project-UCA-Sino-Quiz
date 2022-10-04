from .views import home, register, all_categories, category_quiz, submit_answer
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('accounts/register', register, name='register'),
    path('all-categories', all_categories, name='all_categories'),
    path('category-quiz/<int:category_id>', category_quiz, name='category_question'),
    path('submit_answer/<int:category_id>/<int:quest_id>', submit_answer, name='submit_answer')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
