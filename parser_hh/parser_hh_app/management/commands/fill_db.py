from django.core.management.base import BaseCommand
from parser_hh_app.models import Code_Region, Vacancy, Skill
from parser_hh_app.main import Parser

result_sort = sorted(Parser().skills().items(), key=lambda x: x[1], reverse=True)


class Command(BaseCommand):

    def handle(self, *args, **options):
        vacancy = Vacancy.objects.create(name=Parser().vacancy)
        Code_Region.objects.create(name=Parser().area, vacancy=vacancy)
        for skill, count in result_sort:
            # не записываю навыки которые упоминаются 1 раз, думаю, ими можно пока пренебречь
            if int(count) >= 2:
                Skill.objects.create(name=skill, info=count, vacancy=vacancy)
