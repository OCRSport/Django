from .models import Skill, Vacancy
from rest_framework import serializers


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['name', 'info', 'vacancy']


class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['name']
