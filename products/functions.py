import json
PATH_json = r'F:\Python\GB_course\base_django\geekshop\products\fixtures\fixtures.json'


def get_cards(file_path=PATH_json):
    f = open(file_path, encoding='utf-8')
    data = json.loads(f.read())
    f.close()
    return data
