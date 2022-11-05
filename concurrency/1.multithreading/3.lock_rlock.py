import time
import threading

value = 0
locker = threading.Lock() # Lock - общий для всех потоков блокировщик, RLock - блокировщик на каждый поток

def inc_value():
    global value
    while True:
        with locker: # locker.acquire() - block ... locker.release() - unlock
            value += 1
            time.sleep(1)
            print(value)

for _ in range(5):
    threading.Thread(target=inc_value).start()