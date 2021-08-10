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
  
def insertStudent() -> bool:
  # studentsCollection = db.createCollection(name='Students')
  studentCll = db['Students']
  doc1 = studentCll.createDocument({'name': 'Dercio Derone', 'email': 'dercio@gmail.com'})
  doc2 = studentCll.createDocument({'name': 'Paulo Lopes', 'email': 'paulo@gmail.com'})
  doc3 = studentCll.createDocument({'name': 'Anderson Francisco', 'email': 'anderson@gmail.com'})
  doc1.save(); doc2.save(); doc3.save()
  # doc1['name'] = 'Dercio Derone'
  # doc1['email'] = 'derciosinione@gmail.com'
  return True



