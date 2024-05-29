import time
import requests
from xml.etree import ElementTree as ET


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Currencies:
    def __init__(self, lst=None):

        self.currencies_list = lst
        self.last_call = 0
        self.res_cache = None
    
    def __del__(self):
        class_name = self.__class__.__name__  
        print(f'\n{class_name} уничтожен')  
        print('Сборщик мусора отработал')

    def __add__(self, currencies):
        self._currencies_list.append(currencies)
        return self

    @property
    def get_currencies(self):

        return self._currencies_list
    
    def __call__(self):

        if time.time() - self.last_call > 1:
            self.res_cache = requests.get(
                'http://www.cbr.ru/scripts/XML_daily.asp')
            self.last_call = time.time()

            result = []

            root = ET.fromstring(self.res_cache.content)
            valutes = root.findall("Valute")

            for v in valutes:
                valute_id = v.get('ID')
                valute = {}
                if (str(valute_id) in self._currencies_list):
                    valute_cur_name, valute_cur_val = v.find(
                        'Name').text, v.find('Value').text
                    valute_charcode = v.find('CharCode').text
                    valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                    result.append(valute)
            return result

            
        else:
            print("\nМинуточку")
            time.sleep(5)
            return "Готово\n"


    @get_currencies.setter
    def currencies_list(self, lst):

        self._currencies_list = lst


if __name__ == '__main__':
    cur = 'R01625'
    res = Currencies(cur)
    print(len(cur))
    for i in range(0, len(cur)):
        print(f'{res()}')