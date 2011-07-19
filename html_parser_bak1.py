# -*- coding: cp936 -*-

from HTMLParser import HTMLParser
import urlparse

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)


        #��Ա��Ϣ
        self.playerinfo =  {u"simplified_name"  : "",\
                            u"traditional_name" : "",\
                            u"english_name"     : "",\
                            u"tallness"         : "",\
                            u"weight"           : "",\
                            u"country"          : "",\
                            u"birthday"         : "",\
                            u"previous_team"    : "",\
                            u"photo"            : ""\
                            }

        #ʶ����Ա��Ϣ�� "�ؼ���"
        self.keywords =    ("label_namej",\
                            "label_namef",\
                            "label_namee",\
                            "label_country",\
                            "label_weight",\
                            "label_tallness",\
                            "label_birthday",\
                            "label_CTeam"\
                            )

        #ʶ����Ƭ�� "�ؼ���"
        self.photokeyword = ("imgphoto")


        #"�ؼ���"�� "��Ա��Ϣ�ֵ��key" �� ӳ��
        self.map = {"label_namej"    :    u"simplified_name",\
                    "label_namef"    :    u"traditional_name",\
                    "label_namee"    :    u"english_name",\
                    "label_country"  :    u"country",\
                    "label_weight"   :    u"weight",\
                    "label_tallness" :    u"tallness",\
                    "label_birthday" :    u"birthday",\
                    "label_CTeam"    :    u"previous_team",\
                    "imgphoto"       :    u"photo"\
                    }



        #��һ����ǩ
        self.tag = ""


        #handle_data()������
        self.trigger = 0

    def handle_starttag(self,tag,attrs):
        if tag == "span":
            for (name,value) in attrs:
                if value in self.keywords:
                    #ӳ���ֵ������
                    self.tag = self.map[value]
                    #���ô�����
                    self.trigger = 1

     ###########
        if tag == "img":

            photourl = ""

            for (name,value) in attrs:
                if name == "src":
                    photourl = value

                if value in self.photokeyword:
                    self.tag = self.map[value]
                    self.trigger = 1

            if self.trigger == 1:
                self.playerinfo[self.tag] = urlparse.urljoin(\
                                            'http://info.bet007.com/image/',\
                                            photourl
                                            )
                photourl
                self.trigger = 0
     ########

    def handle_endtag(self,tag):
        if tag == "span" and self.trigger == 1:
            #����������
            self.trigger = 0


    def handle_data(self,data):
        '''������Ϊ1ʱ,��ȡ����;���߲�ȡĬ��ֵ.'''
        if self.trigger == 1:
            self.playerinfo[self.tag] = data






















##if __name__ == "__main__":
##
##    from guolv import formatHTML
##    from domtree import xmltree
##
##    #����html�ļ�,��ʽ��
##    path = r"C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\player.html"
##    html_code=open(path,'r')
##    data = html_code.read()
##    data = formatHTML(data)
##    print data
##
##    #����,��ȡ����
##    hc = MyHTMLParser()
##    hc.feed(data)
##    hc.close
##
####    #��ӡ
####    for key in hc.playerinformation.keys():
####        print key,type(key),hc.playerinformation[key],type(hc.playerinformation[key])
####
####    print "ok"
##
##    #����DOM��
##    import xml.dom.minidom
##    impl = xml.dom.minidom.getDOMImplementation()
##    dom = impl.createDocument(None,'catalog',None)
##
##    #
##    xmlt = xmltree(dom)
##    xmlt.insert_player_record(hc.playerinformation)
##
##    print xmlt.dom.toprettyxml()
##    print "end"
##
##
