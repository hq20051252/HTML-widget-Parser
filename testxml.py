class xml_printer:
    def __init__(self,output_file):
        
        import os
        import xml.dom.minidom
        
        if os.path.isfile(output_file):
            self.dom = xml.dom.minidom.parse(output_file)
        
        self.impl = xml.dom.minidom.getDOMImplementation()
        self.dom = self.impl.createDocument(None,'Player',None)
        
        



    #创建基本节点
    def makeEasyTag(self,dom,tagname,value):
        tag = self.dom.createElement(tagname)

        text = self.dom.createTextNode(value)

        tag.appendChild(text)

        return tag

    #创建个人信息节点
    def makeper_info_node(dom,playerinfo):
        tag = dom.createElement(playerinfo["姓名"])
    
        #循环创建个人信息元素,姓名,国家,....
        for key in playerinfo.keys():
            childnode = makeEasyTag(dom,key,playerinfo[key])
            tag.appendChild(childnode)

        return tag
