from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt import tokens
from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf
from .serializers import RegistrationSerializer, LoginSerializer

# Create your views here.

def get_user_tokens(user):
    """ Generates user tokens for authentication. """
    refresh = tokens.RefreshToken.for_user(user)
    return {
        "refresh_token": str(refresh),
        "access_token": str(refresh.access_token)
    }

class RegisterView(APIView):
    def post(self, request):
        """
        Handles the POST request for user registration.
        First check the data using serializer. If the data is valid, save the user and return the response.
        If the data is not valid, return the error message.
        """
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user is not None:
                return Response({'status':'Registered', 'data':serializer.data}, status=status.HTTP_201_CREATED)
                        
        return Response({'detail': 'Invalid Credentials!'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        """
        Handles the POST request for user login.
        First check the data using serializer. If the data is valid, authenticate the user.
        If the user is authenticated, generate access and refresh tokens and return them in the response.
        """
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):        
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)

        if user is not None:
            tokens = get_user_tokens(user)
            res = Response()
            res.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=tokens['access_token'],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )

            res.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],
                value=tokens['refresh_token'],
                expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            
            res.data = tokens
            res['X-CSRFToken'] = csrf.get_token(request)
            return res
        
        return Response({'detail': 'Invalid Credentials!'}, status=status.HTTP_401_UNAUTHORIZED)