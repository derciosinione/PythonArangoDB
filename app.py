from os import name
from typing import Any
import pyArango.connection as adb


cnx = adb.Connection(arangoURL='http://172.16.16.36:8529/',username='root', password='snirdb@2021')

db = Any
def getDB(str: name) -> bool:
  if not cnx.hasDatabase(name=name):
    op = input('This database does not exists, do you want to create? (Y/n)')
    if op == 'Y' or op == 'y':
      db = cnx.createDatabase(name=name)
    else: return False
  else:
    db = cnx[name]
  return True

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

