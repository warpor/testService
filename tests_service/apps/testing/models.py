from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    active = models.BooleanField()

    def __str__(self):
        return self.title
# Create your models here.
