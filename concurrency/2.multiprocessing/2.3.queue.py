import multiprocessing
import random

queue = multiprocessing.Queue() # shared очередь

def process_func(q):
    val = random.randint(0, 10)
    q.put(str(val))

if __name__ == '__main__':
    prc_list = []

    for _ in range(10):
        pr = multiprocessing.Process(target=process_func, args=(queue,))
        prc_list.append(pr)
        pr.start()

    for i in prc_list:
        i.join()

    for el in iter(queue.get, None):
        print(el)
