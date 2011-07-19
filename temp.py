import MySQLdb
import sql_spec


q = sql_spec.connect('localhost','root','88888888','qiud')
qcur= q.cursor()

qcur.execute('''select player_id from playerinfo''')
result = qcur.fetchall()

fd = open('record.txt','w')

for r in result:
    fd.write(r[0]+'\n');
    
