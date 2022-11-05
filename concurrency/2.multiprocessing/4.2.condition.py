import time
import multiprocessing

cond = multiprocessing.Condition()

def prc1_function():
    print('функция prc1_function запущена!')
    while True:
        with cond:
            cond.wait()
            print('Получили событие')
            
def test_cond():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f'test_cond: {i}')
        time.sleep(1)

if __name__ == '__main__':
    multiprocessing.Process(target=prc1_function).start()
    multiprocessing.Process(target=test_cond).start()