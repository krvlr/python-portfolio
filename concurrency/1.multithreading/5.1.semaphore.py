import time
import random
from threading import Thread, BoundedSemaphore, current_thread

pool = BoundedSemaphore(5) # максимальное количество исполняемых потоков в очереди семафора

def thread_func():
    with pool:
        slp = random.randint(1, 5)
        print(f'{current_thread().name} - sleep({slp})')
        time.sleep(slp)

for i in range(10):
    Thread(target=thread_func, name=f'thr-{i}').start()