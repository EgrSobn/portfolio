import json
import pandas
import requests
from xml.etree import ElementTree as ET


class BaseCurrenciesList():
    def get_currencies(self, currencies_ids_lst: list) -> dict:
        pass


class CurrenciesList(BaseCurrenciesList):
    def __init__(self, lst=None):

        self.currencies_list = lst

    def __add__(self, currencies):

        if currencies in self._currencies_list:
            print(f'Error: Валюта {currencies} уже есть в списке')
        else:
            self._currencies_list.append(currencies)
        return self

    def __sub__(self, currencies):

        if currencies in self._currencies_list:
            self._currencies_list.remove(currencies)
        else:
            print(f'Error: Валюты {currencies} нет в списке')
        return self

    @property
    def get_currencies(self):

        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        result = []

        root = ET.fromstring(cur_res_str.content)
        valutes = root.findall("Valute")

        for _v in valutes:
            valute_id = _v.get('ID')
            valute = {}
            if (str(valute_id) in self._currencies_list):
                valute_cur_name, valute_cur_val = _v.find(
                    'Name').text, _v.find('Value').text
                valute_charcode = _v.find('CharCode').text
                valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                result.append(valute)

        return result

    @get_currencies.setter
    def currencies_list(self, lst):

        self._currencies_list = lst


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

    def get_currencies(self) -> dict:
        return self.__wrapped_object.currencies_list


class ConcreteDecoratorJSON(Decorator):
    def get_currencies(self) -> str:
        return f"ConcreteDecoratorJSON({json.dumps(self.wrapped_object.currencies_list, indent=4, ensure_ascii=False)})"


class ConcreteDecoratorCSV(Decorator):
    def get_currencies(self) -> str:
        res = json.dumps(self.wrapped_object.currencies_list, indent=4, ensure_ascii=False)
        return f"ConcreteDecoratorCSV({pandas.read_json(res).to_csv()})"




def show_currencies(currencies: BaseCurrenciesList):

    print(currencies.currencies_list)


if __name__ == "__main__":

    curlistdict = CurrenciesList(['R01335', 'R01700J'])
    print("Client: I've got a simple component:")
    show_currencies(curlistdict)

    print("\n")
    wrappedcurlist = Decorator(curlistdict)
    wrappedcurlist_json = ConcreteDecoratorJSON(curlistdict)
    print(wrappedcurlist_json.get_currencies())

    print("\n")
    wrappedcurlist_csv = ConcreteDecoratorCSV(curlistdict)
    print(wrappedcurlist_csv.get_currencies())
