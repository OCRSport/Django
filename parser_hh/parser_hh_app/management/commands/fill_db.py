from django.core.management.base import BaseCommand
from parser_hh_app.models import Code_Region, Vacancy, Skill
from parser_hh_app.main import parser, result_sort


class Command(BaseCommand):

    def handle(self, *args, **options):
        vacancy_bd = Vacancy.objects.create(name=parser.vacancy)
        Code_Region.objects.create(name=parser.area, vacancy=vacancy_bd)
        for skill, count in result_sort:
            Skill.objects.create(name=skill, info=count, vacancy=vacancy_bd)
