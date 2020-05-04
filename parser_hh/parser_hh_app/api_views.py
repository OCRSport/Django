from .models import Skill, Vacancy
from rest_framework import routers, serializers, viewsets
from .serializers import SkillSerializer, VacancySerializer


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
