import time
from threading import Thread


class MyThread(Thread):


    def __init__(self):
        Thread.__init__(self)
        self.active = True
        self.secs = 0

    def run(self):
        global secs,active
        while(True):
            if self.active == False:
                break
            self.secs += 1
            time.sleep(1)

    def kill_thread(self):
        self.active = False

def create_thread():
        my_thread = MyThread()
        my_thread.start()
        return my_thread