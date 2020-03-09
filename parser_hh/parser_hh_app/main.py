from parser_hh_app.parser import Parser

vacancy = input('Введите вакансию для поиска (по умолчанию - python developer): ')
if not vacancy:
    vacancy = 'python developer'
area = input('Введите регион для поиска (по умолчанию - Москва (1)): ')
if not area:
    area = '1'
parser = Parser(vacancy, area)
result_sort = sorted(parser.skills().items(), key=lambda x: x[1], reverse=True)
