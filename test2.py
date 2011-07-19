# -*- coding: cp936 -*-

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)


        #��Ա��Ϣ
        self.playerinformation = {}

        #�ؼ���
        self.keywords = ("label_namej","label_namef","label_namee","label_country","label_weight","label_tallness","label_birthday","label_CTeam")
        self.map = {"label_namej":u"������","label_namef":u"������","label_namee":u"Ӣ����","label_country":u"����","label_weight":u"����","label_tallness":u"���","label_birthday":u"����","label_CTeam":u"��Ч�����"}

        #��һ����ǩ
        self.tag = ""
        #handle_data()������
        self.trigger = 0

    def handle_starttag(self,tag,attrs):
        if tag == "span":
            for name,value in attrs:
                if value in self.keywords:
                    #ӳ���ֵ������
                    self.tag = self.map[value]
                    #���ô�����
                    self.trigger = 1

    def handle_data(self,data):
        if self.trigger == 1:

            self.playerinformation[self.tag] = data
            #����������
            self.trigger = 0

if __name__ == "__main__":

    from guolv import formatHTML
    from domtree import xmltree

    #����html�ļ�,��ʽ��
    path = r"C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\player.html"
    html_code=open(path,'r')
    data = html_code.read()
    data = formatHTML(data)
    print data

    #����,��ȡ����
    hc = MyHTMLParser()
    hc.feed(data)
    hc.close

    #��ӡ
    for key in hc.playerinformation.keys():
        print key,type(key),hc.playerinformation[key],type(hc.playerinformation[key])

    print "ok"

    #����DOM��
    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None,'catalog',None)

    #
    xmlt = xmltree(dom)
    xmlt.insert_player_record(hc.playerinformation)

    print xmlt.dom.toprettyxml()
    print "end"

