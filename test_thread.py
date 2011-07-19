import threading
a = ['d','da','a','b','c','e']
b = set(a)

def test_thread():
    print a.pop()
    a.add('0')

t = threading.Thread(test_thread)
t.start()
p= threading.Thread(test_thread)
p.start()
