from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import ParserUser


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'user_app/login.html'


class UserCreateView(CreateView):
    model = ParserUser
    template_name = 'user_app/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('user:login')
