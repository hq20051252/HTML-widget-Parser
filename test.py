from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

        #�ؼ���
        keywords = ("��������","��������","Ӣ������","����","���أ�","��ߣ�","����","��Ч����ӣ�")

        #�ؼ��ֱ��
        self.key_mark = 0

        #��Ա��Ϣ
        self.Playerinfomation = {}

    def handle_data(self,data):
        print data

if "__name__" == "__main__":

    html_code = open(r"C:\Documents and Settings\qi.he\My Documents\player.html",'r').read()

    #��ӡ
    print html_code



    hp = MyHTMLParser()
    hp.feed(html_code)
    
    
