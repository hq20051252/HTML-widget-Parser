# -*- coding: cp936 -*-

import os
import time
import re
from datatonode import data_to_node


#生成DOM树
import xml.dom.minidom
impl = xml.dom.minidom.getDOMImplementation()
dom = impl.createDocument(None,'catalog',None)


os.chdir('C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\yemian')

a = os.listdir('.')
fd = open(a[0],'r')
##data = fd.read().decode('utf-8')
##print type(data)
##
##m = re.findall(u'<html>',data)
##print len(m)

##def main(fileobject,domobject,filename):
##
##    fd = fileobject
##    dom = domobject
mark = fd.readline()
string = fd.readline ()

cache = []
index = 0

while True:
    if mark == string:
        data = ' '.join(cache[1:])
##        print data
        data_to_node(dom,data)
        index +=1
        print index
##        print dom.toprettyxml()
##        time.sleep(3)

        cache = []
        string = fd.readline()

        if index == 99:
            xmlstore = open('test.xml','w')
            xmlstore.write(dom.toprettyxml().encode('utf-8'))
            xmlstore.close()


    else:
        cache.append(string)
        string = fd.readline()

