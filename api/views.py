from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

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
