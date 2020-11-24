from threading import Thread
import time



class Sleeping_thread(Thread):

    def __init__(self,seconds):
        super().__init__()
        self._seconds = seconds



    def run(self):
        print('Sleeping')
        time.sleep(self._seconds)



t1 = Sleeping_thread(3)
t2 = Sleeping_thread(3)

t1.start()
