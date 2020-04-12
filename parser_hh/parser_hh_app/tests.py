from mixer.backend.django import mixer
from django.test import TestCase
from .models import Vacancy, Code_Region, Skill, FilterManager


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


class FilterManagerTestCase(TestCase):

    def test_get_queryset(self):
        self.all_objects = mixer.blend(Skill, info='1')
        self.assertTrue(self.all_objects)


class SkillsListViewTestCase(TestCase):

    def setUp(self):
        self.skill_list = []
        for i in range(50):
            # Skill.objects.create(name='Igor %s' % i, info=i, vacancy_id=i)
            self.skill_list.append(mixer.blend(Skill))

    def test_pagination_url_exists(self):
        resp = self.client.get('/skill_list/?page=1')
        self.assertEqual(resp.status_code, 302)
