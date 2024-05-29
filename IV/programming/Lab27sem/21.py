import math
import concurrent.futures as ftres
from concurrent.futures import as_completed
from functools import partial


def integrate(f, a, b, *, n_iter=1000):
  dx = 1.0 * (b - a) / n_iter
  sum = 0.5 * (f(a) + f(b))
  for i in range(1, n_iter):
    sum += f(a + i * dx)
  return sum * dx

def integrate_async(f, a, b, *, n_jobs=2, n_iter=1000):

    # из futures необходимо импортировать классы для использования потоков и процессов, и оценить время выполнения интегрирования
    # с их помощью.
    # Используйте высокоуровневые классы для этого, см.
    # https://docs.python.org/3/library/concurrent.futures.html
    # в этом месте необходимо создать объекты этих классов, при этом количество потоков/процессов равняется количеству n_jobs.

    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter = n_iter//n_jobs)
    step = (b - a) / n_jobs
    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    return sum(f.result() for f in ftres.as_completed(fs))

if __name__ == '__main__':
    print (integrate_async(lambda x: math.sin(x), 0, 1, n_jobs=2, n_iter=100))
