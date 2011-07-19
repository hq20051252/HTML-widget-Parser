# -*- coding: cp936 -*-

from HTMLParser import HTMLParser
import urlparse

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)


        #球员信息
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

        #识别球员信息的 "关键字"
        self.keywords =    ("label_namej",\
                            "label_namef",\
                            "label_namee",\
                            "label_country",\
                            "label_weight",\
                            "label_tallness",\
                            "label_birthday",\
                            "label_CTeam"\
                            )

        #识别相片的 "关键字"
        self.photokeyword = ("imgphoto")


        #"关键字"到 "球员信息字典的key" 的 映射
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



        #上一个标签
        self.tag = ""


        #handle_data()触发器
        self.trigger = 0

    def handle_starttag(self,tag,attrs):
        if tag == "span":
            for (name,value) in attrs:
                if value in self.keywords:
                    #映射键值，保存
                    self.tag = self.map[value]
                    #设置触发器
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
            #触发器清零
            self.trigger = 0


    def handle_data(self,data):
        '''触发器为1时,提取数据;否者采取默认值.'''
        if self.trigger == 1:
            self.playerinfo[self.tag] = data






















##if __name__ == "__main__":
##
##    from guolv import formatHTML
##    from domtree import xmltree
##
##    #处理html文件,格式化
##    path = r"C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\player.html"
##    html_code=open(path,'r')
##    data = html_code.read()
##    data = formatHTML(data)
##    print data
##
##    #解析,提取数据
##    hc = MyHTMLParser()
##    hc.feed(data)
##    hc.close
##
####    #打印
####    for key in hc.playerinformation.keys():
####        print key,type(key),hc.playerinformation[key],type(hc.playerinformation[key])
####
####    print "ok"
##
##    #生成DOM树
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
