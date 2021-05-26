#editusers.py
import pdata

def append(user):
    users = []
    users=pdata.read(users,'users')
    print(users)
    users.append(user)
    pdata.write(users,'users')
    print(users)
    return 

def remove(user):
    users = []
    users=pdata.read(users,'users')
    print(users)
    if users.count(user)>0:
        users.remove(user)
        pdata.write(users,'users')
        print(users)
    return 
#    users.remove(x)
#    return datap
#list.count(x)	Возвращает количество элементов со значением x