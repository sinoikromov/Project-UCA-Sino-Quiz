from django.shortcuts import render
from . import forms
from .models import Category, Question, UserSubmittedAnswer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def register(request):
    msg = None
    form = forms.RegisterUser
    if request.method == 'POST':
        form = forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Data has been added'

    return render(request, 'registration/register.html', {'form': form, 'msg': msg})


def all_categories(request):
    category = Category.objects.all()
    return render(request, 'all_category.html', {'category': category})


@login_required
def category_quiz(request, category_id):
    cat_id = Category.objects.get(id=category_id)
    question = Question.objects.filter(category=cat_id).order_by('id').first()
    return render(request, 'category_question.html', {'item': question, 'category': cat_id})


@login_required
def submit_answer(request, category_id, quest_id):
    global quest
    if request.method == 'POST':
        cat_id = Category.objects.get(id=category_id)
        question = Question.objects.filter(category=cat_id, id__gt=quest_id).exclude(id=quest_id). \
            order_by('id').first()
        if 'skip' in request.POST:
            if question:
                quest = Question.objects.get(id=category_id)
                user = request.user
                answer = 'Not Submitted'
                UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
                return render(request, 'category_question.html', {'item': question, 'category': cat_id})
        else:
            quest = Question.objects.get(id=quest_id)
            user = request.user
            answer = request.POST['answer']
            UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
        if question:
            return render(request, 'category_question.html', {'item': question, 'category': cat_id})
        else:
            result = UserSubmittedAnswer.objects.filter(user=request.user)
            skipped = UserSubmittedAnswer.objects.filter(user=request.user, right_answer='Not Submitted').count()
            attempted = UserSubmittedAnswer.objects.filter(user = request.user).exclude(right_answer ='Not Submitted').count()
            print('result', result)
            print('skipped',skipped)
            print('attempted', attempted)
            right_ans = 0
            percentage = 0
            for row in result:
                if row.question.right_opt == row.right_answer:
                    right_ans += 1
            percentage = (right_ans * 100) / result.count()
            UserSubmittedAnswer.objects.all().delete()
            return render(request, 'result.html', {'result': result, 'total_skipped': skipped, 'attempted': attempted,
                                                   'right_ans': right_ans, 'percentage': percentage})
    else:
        return HttpResponse('Method not allowed!!')


'''
cat_id = Category.objects.get(id=category_id)
question = Question.objects.filter(category=cat_id, id__gt=quest_id).exclude(id=quest_id)
'''
