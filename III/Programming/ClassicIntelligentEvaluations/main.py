from typing import List
from mathstats import MathStats

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
    # запускающая функция
    data = read_data(FILE)
    c = count_invoice(data[:5])
    print(f'Всего инвойсов (invoices): {c}')  # 2
  
    c = count_invoice(data[:11])
    print(f'Всего инвойсов (invoices): {c}')  # 5
  
    c = count_invoice(data)
    print(f'Всего инвойсов (invoices): {c}')  # 16522
  
    print('Введите InvoiceNo или InvoiceDate или StockCode')
    c = 'StockCode'
    print(f'Различных инвойсов {count_different_values(data, c)}')

    print(f'Товаров для данного StockCode = 21421: {get_total_quantity(data, 21421)}')
  
    data2 = MathStats(FILE2)
    slice_test1 = data2.data[:2]
  
    print(f'Минимум: {data2.min}, Максимум: {data2.max}')
    
    print(f'{data2.get_mean(slice_test1)} - среднее значение')  # (4500.0, 2952.43)
    print(f'{data2.disp} - дисперсия')
    print(f'{data2.sigma_sq} - среднее квадратическое отклонение')

    
def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for _r in reader:
            row = _r
            # row = {
            #     'InvoiceNo': _r['InvoiceNo'],
            #     'InvoiceDate': _r['InvoiceDate'],
            #     'StockCode': int(_r['StockCode']),
            #     'Quantity': int(_r['Quantity'])
            # }
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    # 1. Создаем список виденных инвойсов (пустой), пробегаемся по
    # data и если в списке нет очередного инвойса, то добавляем его туда
    # в конце считаем сколько элементов в нем есть.

    # 2. Создаем множество и добавляем туда по очереди все встреченные
    # элементы. Поскольку это множество, инвойсы в нем не будут
    # повторяться. В конце считаем сколько элементов.

    # 3. Counter
    from collections import Counter

    # Реализуем получение номер invoices и помещение их в список
    # Переписать через генератор списка
    invoices = []
    for _el in data:
        invoices.append(_el['InvoiceNo'])

    count = len(Counter(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
    """
    Функция должна возвращать число различных значений для столбца key в списке data

    key - InvoiceNo или InvoiceDate или StockCode
    """
    from collections import Counter
    elements_list = [
      element[key] for element in data
    ]
    count = len(Counter(elements_list))
    return count


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    Возвращает общее количество проданного товара для данного stock_code
    """

    result = 0
    # for i in data:
    #   if (i['StockCode'] == stock_code):
    #     result += 1
    for i in data:
      if(int(i["StockCode"]) == stock_code):
        result += int(i["Quantity"])
    return result


if __name__ == "__main__":
    main()
