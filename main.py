import os



from filesplit import filesplit
from html_parser import MyHTMLParser
import tool
from guolv import formatHTML


workpath = r'C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\yemian'
home = r'C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\\'
os.chdir(workpath)
filelist =os.listdir('.')

#this is used for sqlite3.
##import sqlite3
###open the database
##p_conn = sqlite3.connect(home+'qiud.db')
##c_conn = sqlite3.connect(home+'career.db')
###get a cursor
##p_cur = p_conn.cursor()
##c_cur = c_conn.cursor()

##p_cur.execute('''select * from playerinfo''')
##print p_cur.fetchall()


#this is used for mysql.
import MySQLdb
host = 'localhost'
user = 'root'
passwd = '88888888'
db = 'qiud'
qiud_conn = MySQLdb.connect(host,user,passwd,db)
qiud_cur = qiud_conn.cursor()


for name in filelist:
    print name
    fd = open(name,'r')
    data = filesplit(fd,'@newpage@')
    print len(data)

    for page in data[1:]:
        print type(page),len(page)
        if not tool.isplayerpage(page[0]):
            continue
        else:
            playerid = '/'.join(tool.getplayerid(page[0]))

            html = ''.join(page[1:])
            html = formatHTML(html)

            hc = MyHTMLParser()
            hc.feed(html)
            playerinfo = hc.get_playerinfo()
            career = hc.get_career()
            playerinfo = tool.addkeytodict(playerinfo,'player_id',playerid)
            career = tool.addkeytodict(career,'player_id',playerid)
            print playerinfo

            #insert record
            tool.insertplayerinfo(qiud_cur,playerinfo)

            for car_record in career:
                tool.insertcareer(qiud_cur,car_record)
            qiud_conn.commit()






