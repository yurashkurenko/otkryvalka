import db
# rows={}
rows= {'user': 'yurasoft1'}
table='users'
db.insert(table,rows)
rows= {'user': 'yurasoft1-'}
table='users'
db.insert(table,rows)
rows= {'user': 'yurasoft1+'}
table='users'
db.insert(table,rows)

rowsfetch=['id','user']
print(db.fetchall(table,rowsfetch))
rowsfetch=['id']
print(db.fetchall(table,rowsfetch))