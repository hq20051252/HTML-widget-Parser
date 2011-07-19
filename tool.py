import re
import urlparse
import types
import MySQLdb
mark = '@newpage@'
def formatNewline(string):
    p = re.compile(r'@newpage@')
    return p.sub(r'\n@newpage@\n',string)

def has_mark(string):
    return mark in string

def formatfile(fds,fdo):
    while True:
        try :
            newline = fds.next()
        except StopIteration:
            break
        if has_mark(newline):
            newline = formatNewline(newline)

        fdo.write(newline)

def deleteBlankline(fds,fdo):

    data = fds.readlines()
    new = []
    for line in data:
        if line.strip():
            new.append(line)
    fdo.write(''.join(new))

def isplayerpage(urlstring):
    t = urlparse.urlsplit(urlstring)[2].split('/')
    if len(t) == 5:
        return True

def getplayerid(urlstring):
    t = urlparse.urlsplit(urlstring)[2].split('/')
    if len(t) == 5:
        return t[2:4]
    else:
        return None

import sqlite3

def insertplayerinfo(cursor,playerinfo):
    insertstring = "INSERT INTO playerinfo (player_id,name,firstname,\
                lastname,chinesename,alias,nationality,\
                birthday,age,homeland,motherland,\
                position,height,weight,preferredfoot,photo)\
                VALUES (\"%(player_id)s\",\"%(name)s\",\"%(firstname)s\",\
                \"%(lastname)s\",\"%(chinesename)s\",\"%(alias)s\",\"%(nationality)s\",\
                \"%(birthday)s\",\"%(age)s\",\"%(homeland)s\",\"%(motherland)s\",\
                \"%(position)s\",\"%(height)s\",\"%(weight)s\",\"%(preferredfoot)s\",\"%(photo)s\")" % playerinfo

#    print insertstring


    try:
        cursor.execute(insertstring)
        print "Success to Insert Playerinfo!"
    except MySQLdb.IntegrityError:
        pass

def insertcareer(cursor,career):
    insertstring = """INSERT INTO career (year,team,comp,minutes,appearence,lineups,\
                    substitude_in,substitude_out,substitude_on_bench,goal,yellow_card,red_card,\
                    yellow_card_2rd,player_id) \
                    VALUES (\"%(year)s\",\"%(team)s\",\"%(comp)s\",\"%(minutes)s\",\
                    \"%(appearence)s\",\"%(lineups)s\",\"%(substitudein)s\",\"%(substitudeout)s\",\
                    \"%(substitude on bench)s\",\"%(goal)s\",\"%(yellow card)s\",\"%(red card)s\",\
                    \"%(yellow card 2rd)s\",\"%(player_id)s\")""" % career
#    print insertstring

    try:
        cursor.execute(insertstring)
        print "Success to Insert Career Record!"
    except MySQLdb.IntegrityError:
        pass


def addkeytodict(input,key,value):
    if type(input) == types.DictType:
        input[key] = value
        return input
    elif type(input) == types.ListType:
        for name in input:
            name[key] = value
        return input



if __name__ == "__main__":
    import os
    os.chdir('C:\Documents and Settings\qi.he.BJ-850INTER290\My Documents\database')
    l = os.listdir('.')
    for name in l:
        fds = open(name,'r')
        fdo = open('new'+' '+name,'w')
        deleteBlankline(fds,fdo)
        print l.index(name)
        fds.close()
        fdo.close()


