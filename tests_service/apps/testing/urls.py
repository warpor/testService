from django.urls import path

from . import views

app_name = "testing"
urlpatterns = [
    path("welcome_page", views.WelcomeView.as_view(), name="welcome")
]
