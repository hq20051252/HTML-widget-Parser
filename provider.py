def provider(pageQueue):
    import sql_spec
    import MySQLdb
    import tool

    q = sql_spec.connect('119.40.35.7','remote','qwer5678()_+','qiud_materials_db')
    qcur = q.cursor()

    fd = open('id.txt','r')
    data = [record.strip() for record in fd.readlines()]
    fd.close()

    for id  in data:
        selectstring = 'select url,response from t_soccerway_players where id = %s'\
                        %id
        qcur.execute(selectstring)
        result = qcur.fetchone()
        print id
        pageQueue.put(result,block = True)
        print "Ok,more record!"


