from django import forms


class Parser_form(forms.Form):
    vacancy_form = forms.CharField(label='Вакансия')
    area_form = forms.CharField(label='Регион')
