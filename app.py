from os import name
from typing import Any
import pyArango.connection as adb

# self.cnx = adb.Connection(arangoURL='http://172.16.16.36:8529/',username='root', password='snirdb@2021')

class DsArango(object):
  def __init__(self, dbUrl, username, password, dbname) -> None:
    self.cnx = adb.Connection(arangoURL=dbUrl,username=username, password=password)
    self.db = None
    self.getDB(dbname)

  def getDB(self, dbname) -> bool:
    if not self.cnx.hasDatabase(name=dbname):
      op = input('This database does not exists, do you want to create? (Y/n)')
      if op == 'Y' or op == 'y':
        self.db = self.cnx.createDatabase(name=dbname)
      else: return False
    else:
      self.db = self.cnx[dbname]
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


db = DsArango(dbUrl='http://172.16.16.36:8529/', username='root', password='snirdb@2021', dbname='school')
print(db.insertStudent())