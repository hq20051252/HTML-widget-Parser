import threading
a = [1,2,3,4,5,6,7,8,9]
def popstack(s,e):
    while True:
    
        if e.isSet():
            e.wait()
        print 'pop' ,s.pop()

        if len(s) <= 0:
            e.set()

def pushstack(s,e,f):
    while True:
        if not f.isSet():
            s.append('a')
            print 'push',s[-1]
            if len(s) > 9:
                f.set()
            
        if e.isSet():
            s.append('a')
            print 'push',s[-1]
            e.clear()

e = threading.Event()
f = threading.Event()

pp = threading.Thread(target = popstack,args =(a,e))
ps = threading.Thread(target = pushstack,args =(a,e,f))

pp.start()
ps.start()


    
