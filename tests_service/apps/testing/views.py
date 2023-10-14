from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class WelcomeView(LoginRequiredMixin, TemplateView):
    template_name = "testing/welcome_page.html"


def sign_up(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("testing:welcome")
        return render(request, 'registration/register.html',
                      {"form": form})
    return render(request, 'registration/register.html',
                  {"form": UserCreationForm()})
# Create your views here.
