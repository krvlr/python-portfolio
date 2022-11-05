import time
import threading

event = threading.Event() 

def image_handler():
    thr_num = threading.current_thread().name
    print(f'Идет подготовка изображения из потока [{thr_num}]')
    event.wait() # событие, исполнения которого (event.set()) поток будет ожидать на данном шаге
    print('Изображение отправлено')

for i in range(10):
    threading.Thread(target=image_handler, name=str(i)).start()
    print(f'Поток [{i}] запущен!')
    time.sleep(1)

if threading.active_count() >= 10:
    event.set()