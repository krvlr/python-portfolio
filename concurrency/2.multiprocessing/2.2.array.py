import multiprocessing
import random
import time

lock = multiprocessing.Lock()
arr = multiprocessing.Array('i', range(10)) # shared массив из int

def process_func(locker, array, index):
    with locker:
        num = random.randint(0, 20)
        vtime = time.ctime()
        array[index] = num
        print(f'array[{index}] = {num}, sleep = {vtime}')
        time.sleep(num)

process_list = []
    
if __name__ == '__main__':
    for i in range(10):
        pr = multiprocessing.Process(target=process_func, args=(lock, arr, i))
        process_list.append(pr)
        pr.start()
        
    for i in process_list:
        i.join()

    print(list(arr))