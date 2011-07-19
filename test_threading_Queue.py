import threading
from time import sleep
from Queue import Queue
a = Queue(9)

def popstack(a):
    while True:
        print a.get(block =True),a.qsize()
        sleep(1)


def pushstack(a):
    while True:
        a.put('a',block = True)
        print a.qsize()
        sleep(1)

        
pp = threading.Thread(target = popstack,args =(a,))
ps = threading.Thread(target = pushstack,args =(a,))

pp.start()
ps.start()
