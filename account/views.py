from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.

class RegisterView(APIView):
    """
    Handles the POST request for user registration.
    First check the data using serializer. If the data is valid, save the user and return the response.
    If the data is not valid, return the error message.
    """
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user is not None:
                return Response({'status':'Registered', 'data':serializer.data}, status=status.HTTP_201_CREATED)
                        
        return Response({'detail': 'Invalid Credentials!'}, status=status.HTTP_400_BAD_REQUEST)
