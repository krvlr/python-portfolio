import multiprocessing
import random
import time

barrier = multiprocessing.Barrier(5)

def prc_func(bar):
    name = multiprocessing.current_process().name
    sl = random.randint(2, 10)
    print(f'[{name}] - спим {sl} секунд!')
    time.sleep(sl)
    bar.wait()
    print(f'[{name}] - запущен!')

if __name__ == '__main__':
    for i in range(8):
        multiprocessing.Process(target=prc_func, args=(barrier, )).start()
