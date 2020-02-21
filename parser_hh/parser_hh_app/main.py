import requests


class Parser:
    DOMAIN = 'https://api.hh.ru/'
    url = f'{DOMAIN}vacancies'
    vacancy = input('Введите вакансию для поиска (по умолчанию - python developer): ')
    if not vacancy:
        vacancy = 'python developer'
    area = input('Введите регион для поиска (по умолчанию - Москва (1)): ')
    if not area:
        area = '1'

    params = {
        'text': vacancy,
        'area': area,
        'period': 30,  # поставил период за 30 дней
        'page': 10  # не совсем понял смысл этих страниц
    }

    skills = {}
    sum_all_skills = 0

    result = requests.get(url, params=params).json()
    items = result['items']

    for item in items:
        url = item['url']
        result = requests.get(url).json()

        for i in result['key_skills']:
            if i['name'] in skills:
                skills[i['name']] += 1
            else:
                skills[i['name']] = 1

    result_sort = sorted(skills.items(), key=lambda x: x[1])


