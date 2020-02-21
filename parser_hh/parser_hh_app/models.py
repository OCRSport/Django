from django.db import models


# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Code_Region(models.Model):
    name = models.CharField(max_length=16)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=32)
    info = models.IntegerField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

