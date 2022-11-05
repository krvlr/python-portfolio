import time
import threading

def thread_func():
    while True:
        print('timer thread working')
        time.sleep(1)

thr = threading.Timer(interval=5, function=thread_func)
thr.daemon = True
thr.start()


for _ in range(4):
    print('main thread work')
    time.sleep(2)
    # thr.cancel() # отменить выполнение потока до начала (interval)

print('finish!')