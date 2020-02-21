from django.core.management.base import BaseCommand
from parser_hh_app.models import Code_Region, Vacancy, Skill
from parser_hh_app.main import Parser

parser = Parser


class Command(BaseCommand):

    def handle(self, *args, **options):
        vacancy = Vacancy.objects.create(name=parser.vacancy)
        Code_Region.objects.create(name=parser.area, vacancy=vacancy)
        for skill, count in parser.result_sort:
            Skill.objects.create(name=skill, info=count, vacancy=vacancy)


