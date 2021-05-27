#edituserboxes.py
import pdata

def append(user,box):
    userboxes = []
    userboxes=pdata.read(userboxes,'userboxes')
    #print(userboxes)
    if box=='':
        userboxes.append([user])
        pdata.write(userboxes,'userboxes')
    for i in range(len(userboxes)):
        if userboxes[i][0]==user:
           userboxes[i].append(box) 
    print(userboxes)
    return 

def remove(user,box):
    userboxes = []
    userboxes=pdata.read(userboxes,'userboxes')
    print(userboxes)
    for i in range(len(userboxes)):
        if userboxes[i][0]==user:
            if userboxes[i].count(box)>0:
                userboxes[i].remove(box)
    print(userboxes)
    return 

def removeuser(user):
    userboxes = []
    userboxes=pdata.read(userboxes,'userboxes')
    print(userboxes)
    for i in range(len(userboxes)):
        if userboxes[i][0]==user:
            userboxes.remove([user])
    print(userboxes)
    return
#    users.remove(x)
#    return datap
#list.count(x)	Возвращает количество элементов со значением x