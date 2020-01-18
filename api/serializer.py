from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework import exceptions

class UserLogin(serializers.ModelSerializer):
    email=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('email','password')

    def validate(self,data):
        email=data.get('email')
        password=data.get('password')
        if email and password:
            auth=authenticate(email=email,password=password)
            if auth:
                return auth
            else:
                raise  exceptions.ValidationError('Email or Password Invalid')
        else:
            raise exceptions.ValidationError('fill all the fields')


