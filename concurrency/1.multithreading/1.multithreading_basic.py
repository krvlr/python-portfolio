import time
import threading

def thread_func(data, n):
    for _ in range(n):
        print(f'[{threading.current_thread().name}] - {data}')
        time.sleep(5)

threads_list = []

for i in range(3): # создаем и запускаем 3 потока
    thr = threading.Thread(target=thread_func, args=(str(time.time()), 10, ), name=f'thr-{i}')
    threads_list.append(thr)
    thr.start()

for i in range(30):
    print("current:", i)
    time.sleep(1)

    if i % 10 == 0: # выводим информацию о потоках
        print('active thread:', threading.active_count())
        print('enumerate:', threading.enumerate())
        print('thr-0 is alive:', threads_list[0].is_alive())

for thr in threads_list:
    thr.join() # ожидаем окончания работы потоков

print('finish!')