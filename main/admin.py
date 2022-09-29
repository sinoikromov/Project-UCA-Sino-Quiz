from django.contrib import admin
from .models import Category, Question

admin.site.register(Category)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']


admin.site.register(Question, QuestionAdmin)
