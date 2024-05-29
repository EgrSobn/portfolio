def fibonacci_list(n):
    fib_list = [0, 1] # определяем первые два элемента последовательности
    [fib_list.append(fib_list[-1] + fib_list[-2]) for i in range(2, n)]
    return fib_list[:n] # возвращаем список с первыми n элементами ряда

f = fibonacci_list(10)

print(f, '\n') # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def fibonacci_yield(n):
    a, b=0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

f = fibonacci_yield(10)

print(list(f), '\n') # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

import random

class UUID:
    def __init__(self):
        self.hex_digits = '0123456789abcdef'
        self.uuid = ''

    def generate(self):
        for i in range(8):
            self.uuid += random.choice(self.hex_digits)
        self.uuid += '-'
        for i in range(3):
            for j in range(4):
                self.uuid += random.choice(self.hex_digits)
            self.uuid += '-'
        for i in range(12):
            self.uuid += random.choice(self.hex_digits)
        return self.uuid

uuid_generator = UUID()
uuid = uuid_generator.generate()

print(uuid, '\n')

from time import time
import hashlib
import json
class Blockchain:
    def __init__(self):
        self.blocks = []
        self.genesis_block = self.create_block(previous_hash='0') # создаем первый блок
        
    def create_block(self, previous_hash):
        block = {
            'index': len(self.blocks) + 1,
            'timestamp': time(),
            'data': None,
            'previous_hash': previous_hash,
            'hash': None
        }
        # рассчитываем хеш блока
        block['hash'] = self.calculate_hash(block)
        self.blocks.append(block)
        return block
    
    def calculate_hash(self, block):
        # рассчитываем хеш блока на основе его параметров
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def generator(self):
        previous_block = self.genesis_block
        while True:
            data = yield
            block = self.create_block(previous_block['hash'])
            block['data'] = data
            yield block
            previous_block = block
 
    def get_history(self):
        return self.blocks

bc = Blockchain()
gen = bc.generator()
next(gen)
gen.send('First block data')
block1 = gen.send('Second block data')
gen.send('Third block data')
block2 = gen.send('Fourth block data')

# выводим историю блоков
print(bc.get_history()) 

# Считаем количество слов и их размер
def count_words_and_sizes(input_str):
    word_count = 0
    word_sizes = []
    for word in input_str.split():
        word_count += 1
        word_sizes.append(len(word))
        yield word_count, word_sizes

input_str = 'This is a test sentence'
counts_and_sizes = count_words_and_sizes(input_str)
for count, sizes in counts_and_sizes:
    print("Word count: ", count)
    print("Word sizes: ", sizes)

if __name__ == '__main__':
    test_input_str = 'This is a test sentence'
    assert list(count_words_and_sizes(test_input_str)) == [(1, [4, 2, 1, 4, 8]), (2, [4, 2, 1, 4, 8]), (3, [4, 2, 1, 4, 8]), (4, [4, 2, 1, 4, 8]), (5, [4, 2, 1, 4, 8])]