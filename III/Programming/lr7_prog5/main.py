"""
Использование декоратора
"""
import json
import pandas
import requests
from xml.etree import ElementTree as ET

class BaseCurrenciesList():
    def get_curr(self) -> dict:
        pass


class Currencies(BaseCurrenciesList):
    """
        aka ConcreteComponent
    """
    def __init__(self, lst):
        # как-то инициализировать объект класса
        self.curr_list = lst
        print('\nИнициализация сделана \n')

    def __del__(self):
        class_name = self.__class__.__name__  
        print(f'\n{class_name} уничтожен')  
        print('Сборщик мусора отработал\n')

    def __add__(self, curr):
        self.__curr_list.append(curr)
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
            if (str(valute_id) in self.__curr_list):
                valute_cur_name, valute_cur_val = v.find(
                    'Name').text, v.find('Value').text
                valute_charcode = v.find('CharCode').text
                valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                result.append(valute)

        return result

    @get_curr.setter
    def curr_list(self, lst):
        self.__curr_list = lst

class Decorator(BaseCurrenciesList):
    """
    aka Decorator из примера паттерна
    """

    __wrapped_object: BaseCurrenciesList = None
    def __init__(self, currencies_lst: BaseCurrenciesList):
        self.__wrapped_object = currencies_lst

    @property
    def wrapped_object(self) -> str:
        return self.__wrapped_object

    def get_curr(self) -> dict:
        return self.__wrapped_object.curr_list


# class ConcreteDecoratorJSON(Decorator):
#     def get_curr(self, currencies_ids_lst: list) -> str:  # JSON
#         return f"ConcreteDecoratorJSON({self.wrapped_object.get_curr(currencies_ids_lst)})"


# class ConcreteDecoratorCSV(Decorator):
#     def get_curr(self, currencies_ids_lst: list) -> str:  # CSV
#         return f"ConcreteDecoratorCSV({self.wrapped_object.get_curr(currencies_ids_lst)})"

class ConcreteDecoratorJSON(Decorator):
    def get_curr(self) -> str:
        return f"JSON-обертка({json.dumps(self.wrapped_object.curr_list, indent=6, ensure_ascii=False)})"


class ConcreteDecoratorCSV(Decorator):
    def get_curr(self) -> str:
        res = json.dumps(self.wrapped_object.curr_list, ensure_ascii=False)
        return f"CSV-обертка({pandas.read_json(res).to_csv()})"


    def __str__(self):
        pass



    
def show_curr(Currencies: BaseCurrenciesList):
    """
       aka client_code() 
    """
    print(f'\n{Currencies.curr_list}\n')


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    # simple = ConcreteComponent()
    # print("Client: I've got a simple component:")
    # client_code(simple)
    # print("\n")

    res = Currencies(['R01335', 'R01700J'])
    print("Client: I've got a simple component:")
    show_curr(res)

    wrapped = Decorator(res)
    wrapped_json = ConcreteDecoratorJSON(res)
    print(wrapped_json.get_curr(), "\n")

    wrapped_csv = ConcreteDecoratorCSV(res)
    print(wrapped_csv.get_curr())
    
    # show_currencies(wrappedcurlist_csv)
    # show_currencies(wrappedcurlist)
