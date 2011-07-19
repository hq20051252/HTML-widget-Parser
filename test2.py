# -*- coding: cp936 -*-

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)


        #球员信息
        self.playerinformation = {}

        #关键字
        self.keywords = ("label_namej","label_namef","label_namee","label_country","label_weight","label_tallness","label_birthday","label_CTeam")
        self.map = {"label_namej":u"简体名","label_namef":u"繁体名","label_namee":u"英文名","label_country":u"国籍","label_weight":u"体重","label_tallness":u"身高","label_birthday":u"生日","label_CTeam":u"曾效力球队"}

        #上一个标签
        self.tag = ""
        #handle_data()触发器
        self.trigger = 0

    def handle_starttag(self,tag,attrs):
        if tag == "span":
            for name,value in attrs:
                if value in self.keywords:
                    #映射键值，保存
                    self.tag = self.map[value]
                    #设置触发器
                    self.trigger = 1

    def handle_data(self,data):
        if self.trigger == 1:

            self.playerinformation[self.tag] = data
            #触发器清零
            self.trigger = 0

if __name__ == "__main__":

    from guolv import formatHTML
    from domtree import xmltree

    #处理html文件,格式化
    path = r"C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\player.html"
    html_code=open(path,'r')
    data = html_code.read()
    data = formatHTML(data)
    print data

    #解析,提取数据
    hc = MyHTMLParser()
    hc.feed(data)
    hc.close

    #打印
    for key in hc.playerinformation.keys():
        print key,type(key),hc.playerinformation[key],type(hc.playerinformation[key])

    print "ok"

    #生成DOM树
    import xml.dom.minidom
    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None,'catalog',None)

    #
    xmlt = xmltree(dom)
    xmlt.insert_player_record(hc.playerinformation)

    print xmlt.dom.toprettyxml()
    print "end"

