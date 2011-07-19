# -*- coding: cp936 -*-

import xml.dom.minidom

class xmltree:
    """接受球员信息字典,添加到dom节点树上"""

    def __init__(self,dom,playerinfo):
        self.dom = dom
        self.root = self.dom.documentElement
        self.insert_player_record(playerinfo)



    #创建基本节点
    def makeEasyTag(self,tagname,value):
        tag = self.dom.createElement(tagname)

        text = self.dom.createTextNode(value)

        tag.appendChild(text)

        return tag

    #创建个人信息节点
    def make_per_info_node(self,playerinfo):

#        print playerinfo.has_key(u"english_name")
#        print playerinfo.values()
        tag = self.dom.createElement("player")
        tag.setAttribute(u"english_name",playerinfo[u"english_name"])

        #循环创建个人信息元素,姓名,国家,....
        for key in playerinfo.keys():
            childnode = self.makeEasyTag(key,playerinfo[key])
            tag.appendChild(childnode)

        return tag

    #插入球员信息记录
    def insert_player_record(self,playerinfo):
        player_node = self.make_per_info_node(playerinfo)
        self.root.appendChild(player_node)

    #写到xml文件中
    def writetoxml(self,fileobject,encoding):
        self.dom.toprettyxml()
        writer.close()
































###if __name__== "__main__":
###    playerinfo = {"曾效力球队":"赫尔辛基","体重":"68","英文名":"Mohamed Kamara","国籍":None,"繁体名":"M.卡馬拉","简体名":"M.卡马拉","生日":"1987/11/16","身高":"177"}
###
###    impl = xml.dom.minidom.getDOMImplementation()
###    dom = impl.createDocument(None,'catalog',None)
###
###    xmlt = xmltree(dom)
###    xmlt.insert_player_record(playerinfo)
###
###    print xmlt.dom.toxml()
###    print "end"
