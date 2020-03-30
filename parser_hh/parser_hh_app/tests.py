from mixer.backend.django import mixer
from django.test import TestCase
from .models import Vacancy, Code_Region, Skill


# Create your tests here.
class VacancyTestCase(TestCase):

    def test_str(self):
        self.vacancy = Vacancy.objects.create(name='test_name')
        self.assertEqual(str(self.vacancy), 'test_name')


class Code_RegionTestCase(TestCase):

    def setUp(self):
        self.code_region = mixer.blend(Code_Region, name='test_name')

    def test_str(self):
        self.assertEqual(str(self.code_region), 'test_name')


class SkillTestCase(TestCase):

    def setUp(self):
        self.skill = mixer.blend(Skill, name='test_name')

    def test_str(self):
        self.assertEqual(str(self.skill), 'test_name')
