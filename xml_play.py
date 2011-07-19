# -*- coding: cp936 -*-
import xml.dom.minidom
impl = xml.dom.minidom.getDOMImplementation()
dom = impl.createDocument(None,'catalog',None)

root = dom.documentElement

playerinfo = {"��Ч�����":"�ն�����","����":"68","Ӣ����":"Mohamed Kamara","����":None,"������":"M.���R��","������":"M.������","����":"1987/11/16","���":"177"}

#���������ڵ�
def makeEasyTag(dom,tagname,value):
    tag = dom.createElement(tagname)

    text = dom.createTextNode(str(value))

    tag.appendChild(text)

    return tag

#����������Ϣ�ڵ�
def make_per_info_node(dom,playerinfo):
    tag = dom.createElement(playerinfo["������"])

    #ѭ������������ϢԪ��,����,����,....
    for key in playerinfo.keys():
        print type(playerinfo[key])
        childnode = makeEasyTag(dom,key,playerinfo[key])
        tag.appendChild(childnode)

    return tag

#������Ա��Ϣ��¼
def insert_player_record(dom,playerinfo):
    player_node = make_per_info_node(dom,playerinfo)
    root.appendChild(player_node)
    
insert_player_record(dom,playerinfo)
print dom.toprettyxml()

##f = file('test.xml','w')
##import codecs
##writer =  codecs.lookup('utf-8')[3](f)
##dom.writexml(writer,encoding = 'utf-8')
##writer.close()
##    



    
