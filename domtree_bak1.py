# -*- coding: cp936 -*-

import xml.dom.minidom

class xmltree:
    """������Ա��Ϣ�ֵ�,��ӵ�dom�ڵ�����"""

    def __init__(self,dom,playerinfo):
        self.dom = dom
        self.root = self.dom.documentElement
        self.insert_player_record(playerinfo)



    #���������ڵ�
    def makeEasyTag(self,tagname,value):
        tag = self.dom.createElement(tagname)

        text = self.dom.createTextNode(value)

        tag.appendChild(text)

        return tag

    #����������Ϣ�ڵ�
    def make_per_info_node(self,playerinfo):

#        print playerinfo.has_key(u"english_name")
#        print playerinfo.values()
        tag = self.dom.createElement("player")
        tag.setAttribute(u"english_name",playerinfo[u"english_name"])

        #ѭ������������ϢԪ��,����,����,....
        for key in playerinfo.keys():
            childnode = self.makeEasyTag(key,playerinfo[key])
            tag.appendChild(childnode)

        return tag

    #������Ա��Ϣ��¼
    def insert_player_record(self,playerinfo):
        player_node = self.make_per_info_node(playerinfo)
        self.root.appendChild(player_node)

    #д��xml�ļ���
    def writetoxml(self,fileobject,encoding):
        self.dom.toprettyxml()
        writer.close()
































###if __name__== "__main__":
###    playerinfo = {"��Ч�����":"�ն�����","����":"68","Ӣ����":"Mohamed Kamara","����":None,"������":"M.���R��","������":"M.������","����":"1987/11/16","���":"177"}
###
###    impl = xml.dom.minidom.getDOMImplementation()
###    dom = impl.createDocument(None,'catalog',None)
###
###    xmlt = xmltree(dom)
###    xmlt.insert_player_record(playerinfo)
###
###    print xmlt.dom.toxml()
###    print "end"
