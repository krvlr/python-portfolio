import multiprocessing
import time

# 2 способа создания процесса:
# 1. Создав экземпляр собственного класса, с наследованием от multiprocessing.Process 
# и реализацией функции run()
# 2. Создав функцию и передав её в конструктор класса Process

class NewProcess(multiprocessing.Process):
    def run(self):
        print('work')

def process_func():
    for _ in range(5):
        print(f'{multiprocessing.current_process().name} - {time.time()}')
        time.sleep(1)

if __name__ == '__main__':
    prc_list = []

    for i in range(3):
        prc = multiprocessing.Process(target=process_func, name=f'prc-{i}')
        prc_list.append(prc)
        prc.start()

        print('Процесс запущен')
        print(prc.pid)

    time.sleep(5)
    # prc.terminate() # принудительное завершение процесса

    for prc in prc_list:
        prc.join()
    print('Все процессы завершены!')



