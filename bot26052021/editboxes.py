#editboxes.py
import pdata

def append(box):
    boxes = []
    boxes=pdata.read(boxes,'boxes')
    print(boxes)
    boxes.append(box)
    pdata.write(boxes,'boxes')
    print(boxes)
    return 

def remove(box):
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