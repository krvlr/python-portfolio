import time
import threading

cond = threading.Condition()

def thread_1_func():
    while True:
        with cond:
            cond.wait() # условие, при исполнении которого (cond.notify()) поток будет исполнит нижестоящие инструкции единожды
            print('Получили событие!')

def thread_2_func():
    for i in range(100):
        if i % 10 == 0:
            with cond:
                cond.notify()
        else:
            print(f'f1: {i}')
        time.sleep(0.2)

threading.Thread(target=thread_1_func).start()
threading.Thread(target=thread_2_func).start()