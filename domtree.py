# -*- coding: cp936 -*-

import xml.dom.minidom

class xmltree:
    """接受球员信息字典,添加到dom节点树上"""

    def __init__(self,dom,playerinfo,career):
        self.dom = dom
        self.root = self.dom.documentElement
        if playerinfo:
            self.insert_player_record(playerinfo,career)



    #创建基本节点
    def makeEasyTag(self,tagname,value):
        tag = self.dom.createElement(tagname)

        text = self.dom.createTextNode(value)

        tag.appendChild(text)

        return tag

    #Create a career node;
    def make_career_node(self,career):
        car_node = self.dom.createElement('career')
        for record in career:

            sea_node = self.dom.createElement('season')

            for name in record.keys():
                itemnode = self.makeEasyTag(name,record[name])
                sea_node.appendChild(itemnode)

            car_node.appendChild(sea_node)

        return car_node


    #创建个人信息节点
    def make_per_info_node(self,playerinfo,career,tagname):


        tag = self.dom.createElement(tagname)
        tag.setAttribute('name',playerinfo['name'])

        #循环创建个人信息元素,姓名,国家,....
        for key in playerinfo.keys():
            childnode = self.makeEasyTag(key,playerinfo[key])
            tag.appendChild(childnode)

        tag.appendChild(self.make_career_node(career))

        return tag

    #插入球员信息记录
    def insert_player_record(self,playerinfo,career):
        player_node = self.make_per_info_node(playerinfo,career,'personalInformation')
        self.root.appendChild(player_node)

    #写到xml文件中
    def writetoxml(self,fileobject,encoding):
        self.dom.toprettyxml()
        writer.close()


if __name__== "__main__":
    career = [{'substitude on bench': '?', 'lineups': '?', 'goal': '?', 'comp': '1.l', 'year': '2011/2012', 'yellow card 2rd': '?', 'red card': '?', 'substiudeout': '?', 'team': 'fc schaffhausen', 'appearence': '?', 'yellow card': '?', 'minutes': '?', 'substiudein': '?'}, {'substitude on bench': '1', 'lineups': '9', 'goal': '0', 'comp': 'chl', 'year': '2010/2011', 'yellow card 2rd': '0', 'red card': '0', 'substiudeout': '2', 'team': 'fc schaffhausen', 'appearence': '10', 'yellow card': '1', 'minutes': '814', 'substiudein': '1'}, {'substitude on bench': '?', 'lineups': '?', 'goal': '?', 'comp': 'sul', 'year': '2010/2011', 'yellow card 2rd': '?', 'red card': '?', 'substiudeout': '?', 'team': 'grasshopper', 'appearence': '?', 'yellow card': '?', 'minutes': '?', 'substiudein': '?'}, {'substitude on bench': '0', 'lineups': '6', 'goal': '0', 'comp': 'sul', 'year': '2009/2010', 'yellow card 2rd': '0', 'red card': '0', 'substiudeout': '5', 'team': 'grasshopper', 'appearence': '13', 'yellow card': '1', 'minutes': '505', 'substiudein': '7'}]
    playerinfo = {'motherland': 'serbia and montenegro', 'weight': '74', 'photo': 'http://cache.images.globalsportsmedia.com/soccer/players/150x150/84816.png', 'name': "gianluca d'angelo", 'firstname': 'gianluca', 'lastname': "d'angelo", 'age': '20', 'birthday': '13-3-1991', 'height': '181', 'alias': '', 'chinesename': '', 'homeland': '', 'position': 'midfielder', 'nationality': 'switzerland', 'preferredfoot': 'R'}

    impl = xml.dom.minidom.getDOMImplementation()
    dom = impl.createDocument(None,'catalog',None)

    xmlt = xmltree(dom,playerinfo,career)


    print xmlt.dom.toprettyxml()
    temp = open('text.xml','w')
    temp.write(xmlt.dom.toprettyxml().encode('utf-8'))
    print "end"
