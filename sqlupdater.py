import tool
def updater(resultQueue):
    import MySQLdb
    host = 'localhost'
    user = 'root'
    passwd = '88888888'
    db = 'qiud'
    qiud_conn = MySQLdb.connect(host,user,passwd,db)
    qiud_cur = qiud_conn.cursor()


    while True:
        print "Ser , I am updater!"
        result = resultQueue.get(block = True)
        print result
        playerinfo = result[0]
        print playerinfo
        career = result[1]




        tool.insertplayerinfo(qiud_cur,playerinfo)

        if career:
            for car_record in career:
                tool.insertcareer(qiud_cur,car_record)

        qiud_conn.commit()
        print "I am working,more record be added!"





