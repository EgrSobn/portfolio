import requests
from xml.etree import ElementTree as ET


class Currencies:

    def __init__(self, lst=[]):
        self.__currencies_list = lst
        print('Инициализация прошла успешно\n')

    def __del__(self):
        class_name = self.__class__.__name__  
        print(f'\n{class_name} уничтожен')  
        print('Сборщик мусора отработал')

    def __add__(self, currencies):
        self.__currencies_list.append(currencies)
        return self

    @property
    def get_curr(self):

        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        result = []

        root = ET.fromstring(cur_res_str.content)
        valutes = root.findall("Valute")

        for v in valutes:
            valute_id = v.get('ID')
            valute = {}
            if (str(valute_id) in self.__currencies_list):
                valute_cur_name, valute_cur_val = v.find(
                    'Name').text, v.find('Value').text
                valute_charcode = v.find('CharCode').text
                valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                result.append(valute)

        return result

    @get_curr.setter
    def curr_list(self, lst):

        self.__currencies_list = lst


if __name__ == '__main__':

    res = Currencies(['R01335', 'R01035'])
    print(res.curr_list)

    del res
