from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    active = models.BooleanField()

    def __str__(self):
        return self.title
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    active = models.BooleanField()
    question_text = models.TextField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()
    right_answer = models.BooleanField()

# Create your models here.
