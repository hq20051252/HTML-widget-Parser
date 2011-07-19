import sql_spec
import MySQLdb
import tool

q = sql_spec.connect('119.40.35.7','remote','qwer5678()_+','qiud_materials_db')
qcur = q.cursor()

num = qcur.execute('''select id,url from t_soccerway_players''')
print num


fd = open('record.txt','r')
data = fd.readlines()
data = [record.strip() for record in data]
print len(data)
id_list = []
while True:
    record = qcur.fetchone()

    if record:
        if tool.getplayerid(record[1]):
            print tool.getplayerid(record[1])
            if '/'.join(tool.getplayerid(record[1])) in data:
                pass
            else:
                id_list.append(record[0])
                print tool.getplayerid(record[1])
    else:
        break




fdo = open('id.txt','w')
for id in id_list:

    fdo.write(str(id)+"\n")
print len(id_list)
fdo.close()

