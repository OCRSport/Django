import requests

DOMAIN = 'https://api.hh.ru/'


class Parser:

    def __init__(self, vacancy, area):
        self.vacancy = vacancy
        self.area = area

    def skills(self):
        url = f'{DOMAIN}vacancies'
        params = {
            'text': self.vacancy,
            'area': self.area,
            'period': 30,  # поставил период за 30 дней
            'page': 10  # не совсем понял смысл этих страниц
        }

        skills = {}
        # sum_all_skills = 0

        result = requests.get(url, params=params).json()
        items = result['items']

        for item in items:
            url = item['url']
            result = requests.get(url).json()

            # if result['salary']:
            #     val = item['salary']
            #     if val['from']:
            #         salary.append(val['from'])

            for i in result['key_skills']:
                if i['name'] in skills:
                    skills[i['name']] += 1
                else:
                    skills[i['name']] = 1
        return skills

