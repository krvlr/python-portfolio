import multiprocessing

def process_func(val):
    print(f'[{multiprocessing.current_process().name}] value: {val}')
    return val

def end_func(rs):
    print('Задание завершено!')
    print(rs)

if __name__ == '__main__':
    with multiprocessing.Pool(multiprocessing.cpu_count()) as p: # Пул из процессов по числу ядер процессора
        # p.map(process_func, list(range(100)))
        p.map_async(process_func, list(range(100)), callback=end_func)
        p.close()
        p.join()

    with multiprocessing.Pool(multiprocessing.cpu_count()) as p:
        for i in range(10):
            p.apply_async(process_func, args=(i, ), callback=end_func)
        p.close()
        p.join()