import multiprocessing

def prc_func(m_dict, m_array):
    m_dict['name'] = 'test'
    m_dict['vers'] = 1.0
    m_array.append(1)
    m_array.append(2)
    
if __name__ == '__main__':
    with multiprocessing.Manager() as m:
        d = m.dict()
        l = m.list()

        pr = multiprocessing.Process(target=prc_func, args=(d, l, ))
        pr.start()
        pr.join()

        print('dict:', d)
        print('list:', l)