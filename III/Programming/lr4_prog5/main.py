import itertools as it

'''Задание 1.
Требуется реализовать код для функции fib такой что,
для данного n функция возвращала бы максимальное число элементов
ряда Фибоначчи не превосходящих данное n.'''

def fib(n: int):
    fib_list = [0]
    if n > 1:
        fib_list = [0, 1, 1]
        while (fib_list[-2] + fib_list[-1]) <= n:
            fib_list.append(fib_list[-2] + fib_list[-1])
        return fib_list
    else:
        return fib_list

'''Задание 2.
Дополните код классом FibonacchiLst, который бы позволял перебирать
элементы из ряда Фибоначчи по данному ей списку.
Итератор должен вернуть очередное значение,
которое принадлежит ряду Фибоначчи, из данного ей списка.'''

class FibonacchiList():
    def __init__(self, stop) -> None:
        self.current = 0
        self.next = 1
        self.stop = stop
        self.buffer = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.buffer = self.current
        self.current, self.next = self.next, self.current + self.next
        if self.buffer <= self.stop:
            return self.buffer
        else:
            raise StopIteration

'''Задание 3 + 4.
Для выполнения задания требуется написать такую функцию fib_iter,
которая принимала бы iterable-объект с числами
и возвращала бы числовые значения (принадлежащие ряду Фибоначчи)
с помощью модуля itertools (например, с помощью метода islice()):
кроме того функция является генератором'''

def FibonacchiListGen():
    current, next = 0, 1
    while True:
        yield current
        current, next = next, current + next

if __name__ == '__main__':
    print(f'Задание 1:\n{fib(13)}')
    print(f'Задание 2:\n{list(FibonacchiList(13))}')
    print(f'Задание 3 + 4:\n{list(it.islice(FibonacchiListGen(), 8))}')