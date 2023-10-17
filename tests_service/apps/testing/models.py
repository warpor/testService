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
# Create your models here.
