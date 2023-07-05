from django.shortcuts import render
from .models import Quiz, Question, Answer
from .serializers import QuizSerializers, QuestionSerializers, AnswerSerializers, GetQuestionSerializers, GetQuizSerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetQuizSerializers
        return QuizSerializers

    

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetQuestionSerializers
        return QuestionSerializers
    
    

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers

    