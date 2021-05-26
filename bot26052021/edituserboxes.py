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
    boxes = []
    boxes=pdata.read(boxes,'boxes')
    print(boxes)
    if boxes.count(box)>0:
        boxes.remove(box)
        pdata.write(boxes,'boxes')
        print(boxes)
    return 
#    users.remove(x)
#    return datap
#list.count(x)	Возвращает количество элементов со значением x