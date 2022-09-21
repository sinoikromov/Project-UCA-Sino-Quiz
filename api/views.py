from rest_framework import generics
from quiz.models import Quiz, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestion(APIView):
    def get(self, request,  **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):
    def get(self, request, **kwargs):
        question = Question.objects.filter(quiz__title = kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
