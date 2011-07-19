class xml_printer:
    def __init__(self,output_file):
        
        import os
        import xml.dom.minidom
        
        if os.path.isfile(output_file):
            self.dom = xml.dom.minidom.parse(output_file)
        
        self.impl = xml.dom.minidom.getDOMImplementation()
        self.dom = self.impl.createDocument(None,'Player',None)
        
        



    #���������ڵ�
    def makeEasyTag(self,dom,tagname,value):
        tag = self.dom.createElement(tagname)

        text = self.dom.createTextNode(value)

        tag.appendChild(text)

        return tag

    #����������Ϣ�ڵ�
    def makeper_info_node(dom,playerinfo):
        tag = dom.createElement(playerinfo["����"])
    
        #ѭ������������ϢԪ��,����,����,....
        for key in playerinfo.keys():
            childnode = makeEasyTag(dom,key,playerinfo[key])
            tag.appendChild(childnode)

        return tag
