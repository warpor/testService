from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "testing"
urlpatterns = [
    path("registration/", views.sign_up, name="registration"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("welcome_page", views.WelcomeView.as_view(), name="welcome")
]
