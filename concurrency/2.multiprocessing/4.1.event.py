import multiprocessing
import time

event = multiprocessing.Event() 

def prc1_function():
    print('функция prc1_function запущена!')
    while True:
        # event.wait() # waiting while event not True
        print('process calc, event.is_set():', event.is_set())
        time.sleep(0.5)

def test_event():
    while True:
        time.sleep(2)
        event.set()
        print('set event (True)')
        time.sleep(2)
        event.clear()
        print('clear event (False)')

if __name__ == '__main__':
    print('program started')
    multiprocessing.Process(target=prc1_function).start()
    multiprocessing.Process(target=test_event).start()