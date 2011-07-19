# -*- coding: cp936 -*-
import xml.dom.minidom
impl = xml.dom.minidom.getDOMImplementation()
dom = impl.createDocument(None,'catalog',None)

root = dom.documentElement

playerinfo = {"曾效力球队":"赫尔辛基","体重":"68","英文名":"Mohamed Kamara","国籍":None,"繁体名":"M.卡馬拉","简体名":"M.卡马拉","生日":"1987/11/16","身高":"177"}

#创建基本节点
def makeEasyTag(dom,tagname,value):
    tag = dom.createElement(tagname)

    text = dom.createTextNode(str(value))

    tag.appendChild(text)

    return tag

#创建个人信息节点
def make_per_info_node(dom,playerinfo):
    tag = dom.createElement(playerinfo["简体名"])

    #循环创建个人信息元素,姓名,国家,....
    for key in playerinfo.keys():
        print type(playerinfo[key])
        childnode = makeEasyTag(dom,key,playerinfo[key])
        tag.appendChild(childnode)

    return tag

#插入球员信息记录
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



    
