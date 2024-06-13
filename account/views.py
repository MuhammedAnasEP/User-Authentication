from django.shortcuts import render

# Create your views here.

class LoginView(APIView):
    def post(self, request):
