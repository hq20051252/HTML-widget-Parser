from Queue import Queue
import threading
from provider import provider
import operater
from sqlupdater import updater
import sql_spec
import guolv
import tool


pageQueue = Queue(100)
resultQueue = Queue(50)

prov = threading.Thread(target = provider,args = (pageQueue,))
parser = threading.Thread(target = operater.operater,args = (pageQueue,resultQueue))
sqlupdater = threading.Thread(target = updater,args = (resultQueue,))

prov.start()
parser.start()
sqlupdater.start()

