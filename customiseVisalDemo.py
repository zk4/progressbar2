import time

from progress2 import pb2
import threading

if __name__ == '__main__':


    def userDefineVisual(  tag, nowValue, fullValue):
        percent = float(nowValue) / fullValue
        icons="🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛✅"
        icons_len=len(icons)
        s="%3d%%" % int(round(percent * 100)) if fullValue != nowValue else "    "
        return    f"{tag} {icons[nowValue%(icons_len-1)] if fullValue!=nowValue else icons[-1]} {s}"
    def userDefineVisual2(tag, nowValue, fullValue):
        bar_length = 100
        percent = float(nowValue) / fullValue
        arrow = '#' * int(round(percent * bar_length) - 1) + '#'
        spaces = ' ' * (bar_length - len(arrow))
        return "{2} [{0}] {1}%".format(arrow + spaces, int(round(percent * 100)), tag)
    def go(end):
        name = threading.current_thread().getName()
        p = pb2.getSingleton()
        for i in range(end+1):
            p.update(str(" user defined visual"), i, end,userDefineVisual)
            p.update(str("user defined visual2"), i, end, userDefineVisual2)
            p.update(str(" default Visual"), i, end)
            time.sleep(0.01)

        #important! between pb.start() and pb.end() , if you want to print something, call pb.getSingleton().print.   otherwise you will fuck up the layout
        p.print("print  after ")

    def test():
        p = pb2.getSingleton()
        p.print("start")
        ts=[]
        for i in range(0,2):
            t = threading.Thread(target=go, args=[(i + 1) * 100])
            t.daemon=True
            t.start()
            ts.append(t)

        for t in ts:
            t.join()
        p.update("total", 100, 100)


if __name__ == '__main__':
    p=pb2.getSingleton()
    p.start()
    for i in range(2):
        p.print(f"---------round {i}---------")
        test()

    # for i in range(20):
    #     p.insert_print(str(i))
    #     time.sleep(0.1)
    p.stop()

    print("end")