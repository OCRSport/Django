from django.db import models
from user_app.models import ParserUser


# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=32)
    # user = models.ManyToManyField(ParserUser)

    def __str__(self):
        return self.name


class Code_Region(models.Model):
    name = models.CharField(max_length=16)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    # user = models.ManyToManyField(ParserUser)
    # vacancy = models.ManyToManyField(Vacancy)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=32)
    info = models.IntegerField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    # user = models.ManyToManyField(ParserUser)
    # vacancy = models.ManyToManyField(Vacancy)

    def __str__(self):
        return self.name

