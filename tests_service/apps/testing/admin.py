from django.contrib import admin
import nested_admin
from django import forms
from django.core.exceptions import ValidationError

from .models import Test, Question, Choice, UserRightAnswer


class ChoiceFormSet(forms.models.BaseInlineFormSet):
    def clean(self):
        right_answer_count = 0
        for each_choice in self.forms:
            if each_choice.cleaned_data.get("right_answer"):
                right_answer_count += 1
        if right_answer_count == 0:
            raise ValidationError("There must be at least one right answer")
        if right_answer_count == len(self.forms):
            raise ValidationError("All answers cannot be right")


class ChoicesInLine(nested_admin.NestedTabularInline):
    model = Choice
    extra = 0
    formset = ChoiceFormSet


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    extra = 1
    formset = forms.models.BaseInlineFormSet
    inlines = [ChoicesInLine]

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return 1


@admin.register(Test)
class TestAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        ("Test name", {"fields": ["title"]}),
        ("Test is active", {"fields": ["active"]})
    ]
    inlines = [QuestionInline]

admin.site.register(UserRightAnswer)
# Register your models here.
