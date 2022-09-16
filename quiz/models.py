from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)


class Quiz(models.Model):
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default='New Quiz', verbose_name='Quiz Title')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')
        ordering = ('id',)


class Question(models.Model):
    SCALE = (
        (0, _('Fundamental')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
    )

    quiz = models.ForeignKey(
        Quiz, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_('Type of Question'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_('Difficulty'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Data Created'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active Status'))
    date_updated = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')
        ordering = ('id',)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name=_('answer'), on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_('Answer Text'))
    is_right = models.BooleanField(default=False)
    date_updated = models.DateTimeField(verbose_name=_('Last Updated'), auto_now=True)

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')
        ordering = ('id',)
