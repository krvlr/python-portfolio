import time
import threading

def thread_func(data):
    for _ in range(20):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(1)

thr = threading.Thread(target=thread_func, args=(str(time.time()), ), daemon=True) # Поток daemon будет остановлен сразу после окончания работы программы
# thr.setDaemon(True)
thr.start()
time.sleep(5)
print('finish!')