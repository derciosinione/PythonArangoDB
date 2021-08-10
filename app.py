from os import name
from typing import Any
import pyArango.connection as adb

# self.cnx = adb.Connection(arangoURL='http://172.16.16.36:8529/',username='root', password='snirdb@2021')

class DsArango(object):
  def __init__(self, dbUrl, username, password) -> None:
    self.cnx = adb.Connection(arangoURL=dbUrl,username=username, password=password)
    self.db = None

  def getDB(self, name) -> bool:
    if not self.cnx.hasDatabase(name=name):
      op = input('This database does not exists, do you want to create? (Y/n)')
      if op == 'Y' or op == 'y':
        db = self.cnx.createDatabase(name=name)
      else: return False
    else:
      db = self.cnx[name]
    return True

  def insertStudent(self) -> bool:
    # studentsCollection = db.createCollection(name='Students')
    studentCll = self.db['Students']
    doc1 = studentCll.createDocument({'name': 'Dercio Derone', 'email': 'dercio@gmail.com'})
    doc2 = studentCll.createDocument({'name': 'Paulo Lopes', 'email': 'paulo@gmail.com'})
    doc3 = studentCll.createDocument({'name': 'Anderson Francisco', 'email': 'anderson@gmail.com'})
    doc1.save(); doc2.save(); doc3.save()
    # doc1['name'] = 'Dercio Derone'
    # doc1['email'] = 'derciosinione@gmail.com'
    return True

# getDB('school')
# insertStudent()

db = DsArango()