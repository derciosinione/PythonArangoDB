from os import name
import pyArango.connection as adb


cnx = adb.Connection(arangoURL='http://172.16.16.36:8529/',username='root', password='snirdb@2021')

if not cnx.hasDatabase(name='school'):
  op = input('This database does not exists, do you want to create? (Y/n)')
  if op == 'Y' or op == 'y':
    db = cnx.createDatabase(name='school')
    print('Database created')
else:
  db = cnx['school']
  print('open new connection', db)
  
studentsCollection = db.createCollection(name='Students')

db['Students']