from rest_framework import serializers
from .models import Quiz, Question, Answer


class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description']


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'quiz']
        

class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title', 'question', 'is_correct']


class GetQuestionSerializers(serializers.ModelSerializer):
    list_answers = AnswerSerializers(many=True)

    class Meta:
        model =  Question
        fields = ['id', 'title', 'quiz', 'list_answers']

class GetQuizSerializers(serializers.ModelSerializer):
    list_questions = QuestionSerializers(many=True)

    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'list_questions']





