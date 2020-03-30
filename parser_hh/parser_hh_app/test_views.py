from django.test import Client
from django.test import TestCase
from faker import Faker
from .models import ParserUser


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):

        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/', {'vacancy': self.fake.text(), 'area': self.fake.random_int()})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/contacts/')
        self.assertTrue('name' and 'e_mail' and 'phone' in response.context)

    def test_login_required(self):
        ParserUser.objects.create_user(username='fred', email='test@test.com', password='secret')
        response = self.client.get('/results/')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/skill_list/')
        self.assertEqual(response.status_code, 302)

        self.client.login(username='fred', password='secret')
        response = self.client.get('/results/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/skill_list/')
        self.assertEqual(response.status_code, 200)