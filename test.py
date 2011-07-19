from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

        #关键字
        keywords = ("简体名：","繁体名：","英文名：","国籍","体重：","身高：","生日","曾效力球队：")

        #关键字标记
        self.key_mark = 0

        #球员信息
        self.Playerinfomation = {}

    def handle_data(self,data):
        print data

if "__name__" == "__main__":

    html_code = open(r"C:\Documents and Settings\qi.he\My Documents\player.html",'r').read()

    #打印
    print html_code



    hp = MyHTMLParser()
    hp.feed(html_code)
    
    
