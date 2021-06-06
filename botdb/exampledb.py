import db
import alldatadb
# print(alldatadb.commandlv1(1))
# print(alldatadb.commandlv1(1)[0:4])
i = 5
while i < 15:
    messagetocompare=alldatadb.commandlv1(1)
    print(messagetocompare)
    message=''
    # print(message)
    message=input('Строка для сравнения:')
    print(message)
    #if message.rfind(messagetocompare):

    if message in messagetocompare:
        print('строка входит')
    else:
        print('строка не входит')
# if "dff" in "sdfssf sddff svvsef xbsdf sdfwwe":
    # print u"Входит!"


# rows={}
# rows= {'user': 'yurasoft1'}
# table='users'
# db.insert(table,rows)
# rows= {'user': 'yurasoft1-'}
# table='users'
# db.insert(table,rows)
# rows= {'user': 'yurasoft1+'}
# table='users'
# db.insert(table,rows)

# rowsfetch=['id','user']
# print(db.fetchall(table,rowsfetch))
# rowsfetch=['id']
# rowsfetch=['user']
# print(db.fetchall(table,rowsfetch))

#users={}
#users=db.fetchall('users',['user'])

#print(users)
#['user']
# # [{'user': 'yurasoft10'}, {'user': 'yurasoft10'}, {'user': 'yurasoft10'}, {'user': 'yurasoft10'}, {'user': 'yurasoft10'}, {'user': 'yurasoft10'}, {'user': 'yurasoft1'}, {'user': 'yurasoft1-'}, {'user': 'yurasoft1+'}, #{'user': 'yurasoft1'}, {'user': 'yurasoft1-'}, {'user': 'yurasoft1+'}, {'user': 'yurasoft1'}, {'user': 'yurasoft1-'}, {'user': 'yurasoft1+'}, {'user': 'yurasoft1'}, {'user': 'yurasoft1-'}, {'user': 'yurasoft1+'}, {'user': # #'yurasoft1'}, {'user': 'yurasoft1-'}, {'user': 'yurasoft1+'}]
#username=users[0]
# список словарей

#print(list(username.values())[0])
# выводит yurasoft10


# list юзеров
# users=[]
# users=db.fetchall('users',['user'])
# for j in range(len(users)):
    # print(list(users[j].values())[0])

# yurasoft10
# yurasoft10
# yurasoft10
# yurasoft10
# yurasoft10
# yurasoft10
# yurasoft1
# yurasoft1-
# yurasoft1+
# yurasoft1
# yurasoft1-
# yurasoft1+
# yurasoft1
# yurasoft1-
# yurasoft1+
# yurasoft1
# yurasoft1-
# yurasoft1+
# yurasoft1
# yurasoft1-
# yurasoft1+

#print[username['user']]


# list боксов
# boxes=[]
# boxes=db.fetchall('boxes',['name'])
# for j in range(len(boxes)):
    # print(list(boxes[j].values())[0])
    
    
# C:\install\botdb>py C:\install\botdb\exampledb.py
# 1.2
# 1.1
# 11
# 123
#© 2021 GitHub, Inc.

# list юзеров
#ml=[]
#ml=db.fetchall('menulevel',['ml'])
#print(list(ml[0].values())[0])
#db.updateml("Здравствуйте! Я Ваша тетя.")
#ml=[]
#ml=db.fetchall('menulevel',['ml'])