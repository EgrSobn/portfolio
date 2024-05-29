import timeit
import math
import numpy as np

def integrate(f, a, b, *, n_iter=100):
  # Вычисляем шаг (размер каждой трапеции)
  h = (b - a) / n_iter
  
  # Сумма значений функции на границах интервала
  integral = (f(a) + f(b)) / 2

  # Сумма значений функции внутри интервала
  for i in range(1, n_iter):
      # Вычисляем точку x на текущем шаге
      x = i * h + a
      integral += f(x)

  # Умножаем на шаг
  integral *= h

  return integral

if __name__ == '__main__':
    print(f'Первая {integrate(math.sin, -4, -3)}')
    print(f'Вторая {integrate(math.cos, -4, -3)}')
    print(f'Третья {integrate(math.acos, -1, 1)}')

    print(f'Время выполнения: {timeit.timeit("integrate(math.asin, 0, 1)", setup="from integrator import integrate; import math", number = 100)}')
