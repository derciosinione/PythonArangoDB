import pyArango.connection as adb


cnx = adb.Connection(arangoURL='http://172.16.16.36:8529/',username='root', password='snirdb@2021')

db = cnx.createDatabase(name='school')
if not cnx.hasDatabase(name='school'):
  op = input('This database does not exists, do you want to create? (Y/n)')
  if op is 'Y' or op is 'y':
    cnx.hasDatabase(name='school')
  else:
    pass