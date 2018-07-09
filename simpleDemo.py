import random
import threading
import time

from progress2 import pb2

b=pb2.getSingleton()

def demo():
    for i in range(10):
        tag = threading.current_thread().getName()
        b.update(tag, i, 9)
        time.sleep(0.1*random.randint(0,3))

b.start()
threads=[]
for i in range(0,2):
    t = threading.Thread(target=demo)
    t.daemon=True
    threads.append(t)
    t.start()

for t in threads:
    t.join()
#    order matters
b.stop()
