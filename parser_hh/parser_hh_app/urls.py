from django.urls import path
from parser_hh_app import views

app_name = 'parser_hh_app'

urlpatterns = [
    path('', views.IndexFormView.as_view(), name='index'),
    # path('', views.main_view, name='index'),
    # path('results/', views.results, name='results'),
    path('results/', views.ResultsListView.as_view(), name='results'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('skill_list/', views.SkillsListView.as_view(), name='skill_list')
]
