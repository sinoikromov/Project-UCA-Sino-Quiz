from rest_framework import generics
from .models import Quiz, Question
from .serializers import QuizSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class QuizView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class RandomQuestion(APIView):
    def get(self, request, format: None, **kwargs):
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many = True)
        return Response(serializer.data)
