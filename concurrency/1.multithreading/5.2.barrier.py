import random
import time
import threading

def thread_func(barrier):
    slp = random.randint(3, 7)
    time.sleep(slp)
    print(f'Поток [{threading.current_thread().name}] запущен в ({time.ctime()})')

    barrier.wait()
    print(f'Поток [{threading.current_thread().name}] преодолел барьер в ({time.ctime()})')

barrier = threading.Barrier(5) # задается количество потоков, которые должны дойти до barrier.wait() перед тем как исполнение будет продолжено
for i in range(5):
    threading.Thread(target=thread_func, args=(barrier,), name=f'thr-{i}').start()