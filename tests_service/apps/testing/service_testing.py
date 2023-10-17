from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Test, Question, UserRightAnswer


def session_initialization(test_id: int, request: HttpRequest):
    test: Test = get_object_or_404(Test, pk=test_id)
    request.session["questions_id"] \
        = list(get_active_question(test).values_list("id", flat=True))
    request.session["right_answers"] = 0


def clear_session(request: HttpRequest):
    del request.session["questions_id"]
    del request.session["right_answers"]


def get_active_question(test_objcet: Test):
    return test_objcet.question_set.filter(active=True)
