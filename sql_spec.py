import MySQLdb
import sys
def connect(host,user,passwd,dbname):
    try:
        db = MySQLdb.Connect(host,user,passwd,dbname)
        print "Connect success!\n"
        return db
        
    except MySQLdb.MySQLError:
        print "Failed to connect to the database!"
        sys.exit(1)


def insertplayerinfo(cursor,playerinfo):
    try:
        insertstring = "INSERT INTO playerinfo (player_id,name,firstname,\
                    lastname,chinesename,alias,nationality,\
                    birthday,age,homeland,motherland,\
                    position,height,weight,preferredfoot,photo)\
                    VALUES (\"%(player_id)s\",\"%(name)s\",\"%(firstname)s\",\
                    \"%(lastname)s\",\"%(chinesename)s\",\"%(alias)s\",\"%(nationality)s\",\
                    \"%(birthday)s\",\"%(age)s\",\"%(homeland)s\",\"%(motherland)s\",\
                    \"%(position)s\",\"%(height)s\",\"%(weight)s\",\"%(preferredfoot)s\",\"%(photo)s\")" % playerinfo

        print insertstring


        cursor.execute(insertstring)
    except MySQLdb.OperationalError:
        pass

def insertcareer(cursor,career):
    try:
        insertstring = """INSERT INTO career (year,team,comp,minutes,appearence,lineups,\
                    substitude_in,substitude_out,substitude_on_bench,goal,yellow_card,red_card,\
                    yellow_card_2rd,player_id) \
                    VALUES (\"%(year)s\",\"%(team)s\",\"%(comp)s\",\"%(minutes)s\",\
                    \"%(appearence)s\",\"%(lineups)s\",\"%(substitudein)s\",\"%(substitudeout)s\",\
                    \"%(substitude on bench)s\",\"%(goal)s\",\"%(yellow card)s\",\"%(red card)s\",\
                    \"%(yellow card 2rd)s\",\"%(player_id)s\")""" % career
        print insertstring

        cursor.execute(insertstring)
    except MySQLdb.OperationalError:
        print "Failed to insertion."
        pass
        
