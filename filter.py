# -*- coding: cp936 -*-

import os
import time
import re
from datatonode import data_to_node
from codecs import open as open

count = 0


os.chdir('C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\yemian')

filelist = os.listdir('.')

for name in filelist:
    print name
    #生成DOM树
    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None,'catalog',None)

    fdsource = open(name,'r','utf-8')
    fdoutput = open(name+r'.xml','w','utf-8')

    mark = "@newpage@"
    data = fdsource.readlines()

    cache = []
##    index = 0

    for string in data:

        if mark == string.strip():
#            print 'here'
            data = ' '.join(cache[1:])

            data_to_node(dom,data)
##            index +=1
            count += 1
##            print index
            print count

            cache = []



        else:
            cache.append(string)

    fdoutput.write(dom.toprettyxml())




