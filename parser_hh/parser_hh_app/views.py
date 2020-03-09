from django.shortcuts import render

from .models import Vacancy, Skill, Code_Region
from .form import Parser_form
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from parser_hh_app.parser import Parser


# Create your views here.
def main_view(request):
    if request.method == 'POST':
        form = Parser_form(request.POST)
        if form.is_valid():
            vacancy = form.cleaned_data['vacancy_form']
            area = form.cleaned_data['area_form']
            parser = Parser(vacancy, area)
            return HttpResponseRedirect('/results/')
        else:
            return render(request, 'parser_hh_app/index.html', context={'form': form})
    else:
        form = Parser_form()
        return render(request, 'parser_hh_app/index.html', context={'form': form})


def results(request):
    vacancy = Vacancy.objects.all()
    area = Code_Region.objects.all()
    skill = Skill.objects.all()
    return render(request, 'parser_hh_app/results.html', context={'vacancy': vacancy,
                                                                  'area': area,
                                                                  'skills': skill
                                                                  })


# def contacts(request):
#     name = 'Igor'
#     e_mail = 'igor@mail.com'
#     phone = '123456789'
#     return render(request, 'parser_hh_app/contacts.html', context={'name': name,
#                                                                    'e_mail': e_mail,
#                                                                    'phone': phone
#                                                                    })


class SkillsListView(ListView):
    model = Skill
    template_name = 'skill_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Список ключевых навыков:'
        return context

    def get_queryset(self):
        return Skill.objects.values('name').distinct().filter(info__gte=2)


class Contacts(TemplateView):
    template_name = 'parser_hh_app/contacts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Igor'
        context['e_mail'] = 'igor@mail.com'
        context['phone'] = '123456789'
        return context

    def get_contacts(self, request):
        return render(request, self.template_name)


# class ResultsListView(ListView):
#     skill = Skill
#     vacancy = Vacancy
#     area = Code_Region
#     template_name = 'parser_hh_app/results.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['area'] = Code_Region
#         context['vacancy'] = Vacancy
#         context['skill'] = Skill
#         return context
#
#     def get_queryset(self):
#         return Skill.objects.all(), Vacancy.objects.all()
