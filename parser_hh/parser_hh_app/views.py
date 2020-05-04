from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Vacancy, Skill, Code_Region
from .form import Parser_form
from django.views.generic import ListView, TemplateView, FormView
from django.http import HttpResponseRedirect
from parser_hh_app.parser import Parser


# Create your views here.
# @login_required
# def main_view(request):
#     if request.method == 'POST':
#         form = Parser_form(request.POST)
#         if form.is_valid():
#             vacancy = form.cleaned_data['vacancy_form']
#             area = form.cleaned_data['area_form']
#             # parser = Parser(vacancy, area)
#             # parser.skills()
#             return HttpResponseRedirect('/results/'), vacancy, area
#         else:
#             return render(request, 'parser_hh_app/index.html', context={'form': form})
#     else:
#         form = Parser_form()
#         return render(request, 'parser_hh_app/index.html', context={'form': form})


# def results(request):
#     vacancy = Vacancy.objects.all()
#     area = Code_Region.objects.all()
#     skill = Skill.objects.all()
#     return render(request, 'parser_hh_app/results.html', context={'vacancy': vacancy,
#                                                                   'area': area,
#                                                                   'skills': skill
#                                                                   })


# def contacts(request):
#     name = 'Igor'
#     e_mail = 'igor@mail.com'
#     phone = '123456789'
#     return render(request, 'parser_hh_app/contacts.html', context={'name': name,
#                                                                    'e_mail': e_mail,
#                                                                    'phone': phone
#                                                                    })


class SkillsListView(LoginRequiredMixin, ListView):
    login_url = '/user/login'
    model = Skill
    template_name = 'skill_list.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Список ключевых навыков:'
        return context

    def get_queryset(self):
        return Skill.filter_objects.distinct()


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


class ResultsListView(LoginRequiredMixin, ListView):
    login_url = '/user/login'
    model = Skill
    template_name = 'parser_hh_app/results.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['area'] = Code_Region.objects.all()
        context['vacancy'] = Vacancy.objects.all()
        return context

    def get_queryset(self):
        return Skill.filter_objects.select_related('vacancy').all()
        # return Skill.filter_objects.all()

class IndexFormView(LoginRequiredMixin, FormView):
    template_name = 'parser_hh_app/index.html'
    form_class = Parser_form
    success_url = '/results/'

    def form_valid(self, form):
        vacancy = form.cleaned_data['vacancy_form']
        area = form.cleaned_data['area_form']
        parser = Parser(vacancy, area)
        # не понимаю как result_sort отправить в fill_db.py
        result_sort = sorted(parser.skills().items(), key=lambda x: x[1], reverse=True)
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'парсер hh.ru'
        return context

    def get_title(self, request):
        return render(request, self.template_name)