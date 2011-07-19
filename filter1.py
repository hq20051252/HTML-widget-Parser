# -*- coding: cp936 -*-

#Import building modulars

import os
import time
import re
import codecs


#Import user defined modulars

from datatonode import data_to_node

#Define global varibles
count = 0   #To count record numbers.


os.chdir('C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\yemian')

filelist = os.listdir('.')

for name in filelist:
    #生成DOM树
    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None,'catalog',None)

    fdsource = open(name,'r')
    fdoutput = open(name+r'.xml','w')



    try:
        mark = fdsource.next()
    except StopIteration:
        fdoutput.write(dom.toprettyxml().encode('utf-8'))
        fdoutput.close()
        continue

    string = fdsource.next ()

    cache = []
##    index = 0

    while True:
        if mark == string:
            data = ' '.join(cache[1:])
    ##        print data
            data_to_node(dom,data)
##            index +=1
            count += 1
##            print index
            print count
    ##        print dom.toprettyxml()
    ##        time.sleep(3)

            cache = []
            try:
                string = fdsource.next()
            except StopIteration:
                fdoutput.write(dom.toprettyxml().encode('utf-8'))
                fdoutput.close()
                break


        else:
            cache.append(string)
            try:
                string = fdsource.next()
            except StopIteration:
                fdoutput.write(dom.toprettyxml().encode('utf-8'))
                fdoutput.close()
                break


