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


class FilterManager(models.Manager):

    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(info__gte=1)


class Skill(models.Model):
    objects = models.Manager()
    filter_objects = FilterManager()
    name = models.CharField(max_length=32, db_index=True)
    info = models.IntegerField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    # user = models.ManyToManyField(ParserUser)
    # vacancy = models.ManyToManyField(Vacancy)

    def __str__(self):
        return self.name

