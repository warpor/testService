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
def get_info_about_attemps(right_answer: int,
                           all_question_count: int) -> dict[str, int]:
    test_info = {}
    test_info["right_answer_percent"] \
        = round((100 * (right_answer / all_question_count)), 2)
    test_info["right_answers_count"] = right_answer
    test_info["wrong_answers_count"] \
        = all_question_count - right_answer
    return test_info
