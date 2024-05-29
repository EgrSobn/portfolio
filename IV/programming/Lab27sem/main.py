import threading
import requests
import random
import string



'1.1'

def print_thread_name():
  # Получение имени текущего потока и вывод его на экран
  thread_name = threading.current_thread().name
  print("Имя потока:", thread_name)


def threads_init(func):
  for i in range(5):
    thread = threading.Thread(target=func)
    thread.start()

    if thread.is_alive():
      print(f"Это действительно поток {thread.name}")



'1.2'

def generate_the_name():
  collection = 'abcde'
  name = ''.join(random.choice(collection) for i in range(5))
  return name


def get_img():
  img = requests.get(
      'https://kartinkof.club/uploads/posts/2022-04/1649590989_2-kartinkof-club-p-ugarnie-kartinki-kartinka-ti-super-2.jpg'
  )
  with open(f'./downloads/{generate_the_name()}.jpg', 'wb') as i:
    i.write(img.content)



'1.3'

def req():
  res = requests.get('https://www.google.com/?hl=RU')
  print(f'response from https://www.google.com/?hl=RU: {res.status_code}')



'1.4'

def fact(n):
  res = 1
  for i in range(1, n+1):
    res *= i
  return print(res)

number = 4
threads = []

for i in range(number):
  thread = threading.Thread(target=fact, args=(i+1,))
  thread.start()
  threads.append(thread)

for thread in threads:
  thread.join()


threads_init(print_thread_name)
threads_init(get_img)
threads_init(req)