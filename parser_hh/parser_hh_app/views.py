from django.shortcuts import render
from .models import Vacancy, Skill, Code_Region
from .form import Parser_form


# Create your views here.
def main_view(request):
    if request.method == 'POST':
        form = Parser_form(request.POST)
        if form.is_valid():
            vacancy = form.cleaned_data['vacancy_form']
            area = form.cleaned_data['area_form']
            return vacancy, area
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


def contacts(request):
    name = 'Igor'
    e_mail = 'igor@mail.com'
    phone = '123456789'
    return render(request, 'parser_hh_app/contacts.html', context={'name': name,
                                                                   'e_mail': e_mail,
                                                                   'phone': phone
                                                                   })

