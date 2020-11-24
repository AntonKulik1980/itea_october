from threading import Thread
import time


def io_bound(id, sec):
    print(f'{id} sleep')
    time.sleep(sec)
    print(f'{id} awake')


start = time.time()
t1 = Thread(target=io_bound, args=(1, 1),name = 'Thread-One')
t2 = Thread(target=io_bound, args=(2, 2),name = 'Thread-Two')
t3 = Thread(target=io_bound, args=(3, 3),name = 'Thread-Three')
t1.start()
t2.start()
t3.start()
# print(t1.is_alive())
# t3.join()
# print(time.time() - start)
