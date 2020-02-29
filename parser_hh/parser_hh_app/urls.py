from django.urls import path
from parser_hh_app import views

app_name = 'parser_hh_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('results/', views.results, name='results'),
    path('contacts/', views.contacts, name='contacts')
]