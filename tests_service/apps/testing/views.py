from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class WelcomeView(LoginRequiredMixin, TemplateView):
    template_name = "testing/welcome_page.html"
# Create your views here.
