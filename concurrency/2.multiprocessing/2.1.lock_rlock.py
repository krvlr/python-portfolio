import multiprocessing
import time

lock = multiprocessing.Lock()
r_lock = multiprocessing.RLock()

def process_func(lock, r_lock):
    lock.acquire()
    print(f'Процесс [{multiprocessing.current_process().name}] запущен')
    r_lock.acquire()
    print(f'Процесс [{multiprocessing.current_process().name}] завершился')


if __name__ == '__main__':
    multiprocessing.Process(target=process_func, args=(lock, r_lock), name=f'prc-1').start()
    multiprocessing.Process(target=process_func, args=(lock, r_lock), name=f'prc-2').start()

    time.sleep(2)
    lock.release()
    time.sleep(2)
    r_lock.release() # AssertionError: attempt to release recursive lock not owned by thread
