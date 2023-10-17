from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Test, Question, UserRightAnswer


def session_initialization(test_id: int, request: HttpRequest):
    test: Test = get_object_or_404(Test, pk=test_id)
    request.session["questions_id"] \
        = list(get_active_question(test).values_list("id", flat=True))
    request.session["right_answers"] = 0


def skip_question(request: HttpRequest):
    first_element = request.session["questions_id"].pop(0)
    request.session["questions_id"].append(first_element)  # Add first element in end of list


def clear_session(request: HttpRequest):
    del request.session["questions_id"]
    del request.session["right_answers"]


def finish_test(request: HttpRequest, test_id: int) -> HttpResponseRedirect:
    test: Test = get_object_or_404(Test, pk=test_id)

    save_result(request, test_id)
    right_answer = request.session["right_answers"]
    all_question_count = len(get_active_question(test))
    context = get_info_about_attemps(right_answer, all_question_count)
    clear_session(request)
    return render(request, "testing/result.html", context)


def check_answers(request: HttpRequest, question_id: int):
    user_answers = request.POST.getlist("choice")
    user_answers = set(map(int, user_answers))

    right_answers \
        = get_object_or_404(
        Question, pk=question_id).choice_set.filter(right_answer=True)
    right_answers = set(right_answers.values_list("id", flat=True))

    if right_answers == user_answers:
        request.session["right_answers"] += 1


def get_new_page_with_question(request: HttpRequest, test_id: int):
    question_id = request.session["questions_id"][0]
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "testing/question_answer.html",
                  {"question": question, "test_id": test_id})


def save_result(request: HttpRequest, test_id: int):
    test = get_object_or_404(Test, pk=test_id)
    user_attempt \
        = UserRightAnswer(right_answer=request.session["right_answers"], date=timezone.now(),
                          user=request.user, test=test)
    user_attempt.save()


def get_active_question(test_objcet: Test):
    return test_objcet.question_set.filter(active=True)


def process_all_attempts(tests_history: list[UserRightAnswer], all_question_count: int):
    info_about_prev_attempts = []
    for each_test_history in tests_history:
        test_info = get_info_about_attemps(each_test_history.right_answer,
                                           all_question_count)
        test_info["date"] = each_test_history.date
        info_about_prev_attempts.append(test_info)

    return info_about_prev_attempts


def get_info_about_attemps(right_answer: int,
                           all_question_count: int) -> dict[str, int]:
    test_info = {}
    test_info["right_answer_percent"] \
        = round((100 * (right_answer / all_question_count)), 2)
    test_info["right_answers_count"] = right_answer
    test_info["wrong_answers_count"] \
        = all_question_count - right_answer
    return test_info
