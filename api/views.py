from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializer import UserLogin
from rest_framework.response import Response


# Create your views here.

class LoginView(APIView):
    def post(self, request):
        serelize = UserLogin(data=request.data)
        serelize.is_valid(raise_exception=True)
        objectuser = serelize.validated_data
        token, _ = Token.objects.get_or_create(user=objectuser)
        return Response(token.key, headers={"Access-Control-Allow-Origin": "*"})
