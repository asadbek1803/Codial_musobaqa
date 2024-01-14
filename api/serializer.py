from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.models import Account

from .models import TestModel, Sohalar
from rest_framework import serializers

class ForRegstrationSoha(ModelSerializer):
    class Meta:
        model = Sohalar
        fields = ('name', )

class TestSerializer(ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

class LoginWithToken(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginWithToken, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        soha = ForRegstrationSoha()

        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'soha')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            soha = validated_data['soha']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user