# progressbar2 for python3
# Intro
it`s thread safe. Only One thread will manage the progressBar .

# Tips
 Suppose you want call **print**  in progressBar context.  call **pb2.getSingleton().print()**  instead. otherwise it would mess up the layout 

# Demo
## SimpleDemo
![](https://github.com/zk4/progressbar2/blob/master/1.gif?raw=true)
```
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

b.stop()
```

## Change Visual Demo
![](https://github.com/zk4/progressbar2/blob/master/2.gif?raw=true)
```
def userDefineVisual(  tag, nowValue, fullValue):
    percent = float(nowValue) / fullValue
    icons="🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛✅"
    icons_len=len(icons)
    s="%3d%%" % int(round(percent * 100)) if fullValue != nowValue else "    "
    return    f"{tag} {icons[nowValue%(icons_len-1)] if fullValue!=nowValue else icons[-1]} {s}"
```
call like this
```
pb2.getSingleton().update(str(" user defined visual"), nowValue, endValue,userDefineVisual)
```
see customiseVisalDemo.py


----
 any issues is welcome :)
