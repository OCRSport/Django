from django import forms


class Parser_form(forms.Form):
    vacancy_form = forms.CharField(label='Вакансия', widget=forms.TextInput(attrs={'placeholder': 'enter vacancy',
                                                                                   'class': 'form-control'}))
    area_form = forms.CharField(label='Регион', widget=forms.TextInput(attrs={'placeholder': 'enter area',
                                                                              'class': 'form-control'}))
