import threading

data = threading.local() # создается переменная для каждого потока

def get():
    print(data.value)

def thread_1_func():
    data.value = 111
    get()

    data.value = {'t1 value': 1}
    print('t1:', data.value)

def thread_2_func():
    data.value = 222
    get()

    data.test = ['t2 test: 1']
    print('t2:', data.test)

threading.Thread(target=thread_1_func).start()
threading.Thread(target=thread_2_func).start()