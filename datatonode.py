# --*-- coding:cp936 --*--

import html_parser
from guolv import formatHTML
from domtree import xmltree

def data_to_node(dom,data):
    #Format the HTML page
#    print data
    data = formatHTML(data)
    print 'data to node'
#    print data

    #Parse html page and get information;
    hc = html_parser.MyHTMLParser()
    hc.feed(data)
    hc.close
    playerinfo = hc.get_playerinfo()
    career = hc.get_career()


    xmlt = xmltree(dom,playerinfo,career).dom
