from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField()
    image = models.ImageField(upload_to='cat_imgs/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Question(models.Model):
    SCALE = (
        (0, 'Fundamental'),
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    opt_1 = models.CharField(max_length=200)
    opt_2 = models.CharField(max_length=200)
    opt_3 = models.CharField(max_length=200)
    opt_4 = models.CharField(max_length=200)
    level = models.IntegerField(choices=SCALE, default=0, verbose_name='Difficulty')
    time_limit = models.IntegerField()
    right_opt = models.CharField(max_length=100)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

