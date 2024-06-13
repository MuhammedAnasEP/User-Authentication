from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register', views.RegisterView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('refresh-token', views.CookieTokenRefreshView.as_view(), name='refresh-token'),
]