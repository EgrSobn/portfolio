import threading
import time

def server(barrier):
    print("Сервер: инициализация")
    time.sleep(2)
    print("Сервер: готов")
    barrier.wait() 
    print("Сервер: получен запрос")

def client(barrier):
    print("Клиент: инициализация")
    time.sleep(4)  
    print("Клиент: готов")
    barrier.wait()  
    print("Клиент: отправлен запрос")


barrier = threading.Barrier(2) 
server_thread = threading.Thread(target=server, args=(barrier,))
client_thread = threading.Thread(target=client, args=(barrier,))

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()