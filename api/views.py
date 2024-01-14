from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from accounts.models import Account
from .serializer import TestSerializer,  RegisterSerializer, LoginWithToken
from .models import TestModel
from django.contrib.auth.models import User
# Create your views here.
class QuestionList(generics.ListAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    permission_classes = [
        IsAuthenticated
    ]


class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginWithTokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginWithToken


class TestAnalytics(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        questions = request.data.get('questions')
        answers = request.data.get('answers')

        total = len(questions)
        correct = 0

        for i in range(total):
            if answers[i] == questions[i]['correct_answer']:
                correct += 1

        result = {
            "total": total,
            "correct": correct,
            "percentage": round((correct / total) * 100)
        }

        return Response(result)

