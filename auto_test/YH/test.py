import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name='Python3'):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(100000):
            print("Hello", self.name)
            # time.sleep(1)

