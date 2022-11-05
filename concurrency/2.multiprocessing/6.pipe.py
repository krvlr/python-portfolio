import multiprocessing

def send_data(conn):
    conn.send('data to send')
    # conn.close()

if __name__ == '__main__':
    output_c, input_c = multiprocessing.Pipe()
    multiprocessing.Process(target=send_data, args=(input_c, )).start()
    multiprocessing.Process(target=send_data, args=(input_c, )).start()
    print('data:', output_c.recv())
    print('data:', output_c.recv())