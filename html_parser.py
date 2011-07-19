# --*-- coding:gbk --*--
from HTMLParser import HTMLParser
from convertPlayerinfo  import convertPlayerinfo

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

        #The personal information of players;
        self.playerinfo = []



        #The record of player's career;
        self.playercareer = []

        self.car_record = self.initialRecord()

        #To record footprint.
        self.footprint = []
        #The trigger of handle_data();
        self.trigger = 0
        #Data type mark
        self.datatype = ""
        #key string
        self.keystring = ""


        self.map_car =  {   "season"                                    :"year",\
                            "team"                                      :"team",\
                            "competition"                               :"comp",\

                            "number statistic game-minutes available"   :"minutes",\
                            "number statistic appearances available"    :"appearence",\
                            "number statistic lineups available"        :"lineups",\
                            "number statistic subs-in available"        :"substitudein",\
                            "number statistic subs-out available"       :"substitudeout",\
                            "number statistic subs-on-bench available"  :"substitude on bench",\
                            "number statistic goals available"          :"goal",\
                            "number statistic yellow-cards available"   :"yellow card",\
                            "number statistic 2nd-yellow-cards "        :"yellow card 2rd",\
                            "number statistic red-cards available"      :"red card",\

                            "number statistic game-minutes "             :"minutes",\
                            "number statistic appearances "              :"appearence",\
                            "number statistic lineups "                  :"lineups",\
                            "number statistic subs-in "                  :"substitudein",\
                            "number statistic subs-out "                 :"substitudeout",\
                            "number statistic subs-on-bench "            :"substitude on bench",\
                            "number statistic goals "                    :"goal",\
                            "number statistic yellow-cards "             :"yellow card",\
                            "number statistic red-cards "                :"red card"\

                    }




    def handle_starttag(self,tag,attrs):
        if tag == 'dl':
            self.footprint.append('dl')
#            print self.footprint

        if tag == 'dt':
            if 'dl' in self.footprint:
                self.trigger = 1
                self.datatype = 'playerinfo'
#                print self.footprint

        if tag == 'dd':
            if 'dl' in self.footprint:
                self.trigger = 1
                self.datatype = 'playerinfo'
#                print self.footprint

        if tag == 'div':
            for name,value in attrs:
                if name == u'class' and \
                    value == u'yui-u':
                        self.footprint.append('photo')
#                        print self.footprint

        if tag == 'img' :
            if 'photo' in self.footprint:
                for name,value in attrs:
                    if name == 'src':
                        self.playerinfo.append(value)
#                        print self.footprint


        if tag == 'table':
            for name,value in attrs:
                if name == u'class' and \
                    value == u"playerstats career sortable table":
                    self.footprint.append('table')
#                    print self.footprint
#                    print 'I\'m coming'

        if tag == 'tbody':
            if 'table' in self.footprint:
                self.footprint.append('tbody')





        if tag == 'tr' :
            if 'tbody' in self.footprint:
                self.footprint.append('tr')
#                print self.footprint

        if tag == 'td' :
            if 'tr' in self.footprint:
                for name,value in attrs:
                    if name == 'class':
                        self.keystring = value
                self.trigger = 1
                self.datatype = 'career'
#                print self.footprint

    def handle_endtag(self,tag):
        if tag == 'dl':
            if 'dl' in self.footprint:
                del self.footprint[self.footprint.index('dl')]
#                print self.footprint

        if tag == 'dt':
            if 'dl' in self.footprint:
                self.trigger = 0

        if tag == 'dd':
            if 'dl' in self.footprint:
                self.trigger = 0

        if tag == 'div':
            if 'photo' in self.footprint:
                del self.footprint[self.footprint.index('photo')]
#                print self.footprint

        if tag == 'table':
            if 'table' in self.footprint:
                del self.footprint[self.footprint.index('table')]
#                print self.footprint
#                print 'From here leave'

        if tag == 'tbody':
            if 'table' in self.footprint:
                del self.footprint[self.footprint.index('tbody')]

        if tag == 'tr':
            if 'tbody' in self.footprint:
                self.playercareer.append(self.car_record)
                print 'Another record'
                self.car_record = self.initialRecord()
                del self.footprint[self.footprint.index('tr')]
#                print self.footprint

        if tag == 'td':
            if 'tr' in self.footprint:
                self.trigger = 0
                self.keystring = ""

    def handle_data(self,data):
        if self.trigger == 1:
            if self.datatype == 'career':
                if self.keystring in self.map_car.keys():
                    if data == '?':
                        data = '-1'
                    self.car_record[self.map_car[self.keystring]] = data
                    self.datatype = ""
#                    print 'Get it'
            if self.datatype == 'playerinfo':
                self.playerinfo.append(data)
                self.datatype = ""

    def get_playerinfo(self):
        temp = convertPlayerinfo(self.playerinfo)
        if temp and temp['name'].strip():
            print temp
            return temp

        return None



    def get_career(self):
        return self.playercareer

    def initialRecord(self):
        car_record = { "year":"",\
                        "team":"",\
                        "comp":"",\
                        "minutes":"-1",\
                        "appearence":"-1",\
                        "lineups":"-1",\
                        "substitudein":"-1",\
                        "substitudeout":"-1",\
                        "substitude on bench":"-1",\
                        "goal":"-1",\
                        "yellow card":"-1",\
                        "yellow card 2rd":"-1",\
                        "red card":"-1"\
                    }
        return car_record


if __name__ == "__main__":

    from guolv import formatHTML


    #处理html文件,格式化
    path = r"C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\test.html"
    html_code=open(path,'r')
    data = html_code.read()
    data = formatHTML(data)
    print data

    #解析,提取数据
    hc = MyHTMLParser()
    hc.feed(data)
    hc.close

    print hc.get_career()
    print hc.get_playerinfo()

#    from convertPlayerinfo  import convertPlayerinfo
#    print convertPlayerinfo(hc.playerinfo)
    print 'end'




