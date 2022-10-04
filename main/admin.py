from django.contrib import admin
from .models import Category, Question, UserSubmittedAnswer

admin.site.register(Category)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


admin.site.register(Question, QuestionAdmin)


class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'user', 'right_answer']


admin.site.register(UserSubmittedAnswer, UserSubmittedAnswerAdmin)