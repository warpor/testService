from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from .models import Test, UserRightAnswer
from .service_testing import session_initialization, skip_question, finish_test, check_answers, \
    get_new_page_with_question, get_active_question, process_all_attempts


class WelcomeView(LoginRequiredMixin, ListView):
    model = Test
    template_name = "testing/welcome_page.html"
    context_object_name = "tests_list"

    def get_queryset(self):
        return self.model.objects.filter(active=True)


class InfoView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = "testing/detail.html"

    def get_context_data(self, **kwargs):
        context = super(InfoView, self).get_context_data(**kwargs)
        right = (
            UserRightAnswer.objects.
            filter(user=self.request.user.id, test=self.kwargs["pk"]))
        question_number = len(get_active_question(self.object))
        context["history"] = process_all_attempts(right, question_number)
        context["question_nums"] = [num for num in range(question_number)]
        return context


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
class ResultView(LoginRequiredMixin, TemplateView):
    template_name = "testing/result.html"
