import pdata
global ml
global users
global boxes
global userboxes
ml='top'
users=[]
boxes=[]
userboxes=[]
inputtextstr=''
users=pdata.read(users,'users')
boxes=pdata.read(boxes,'boxes')
userboxes=pdata.read(userboxes,'userboxes')

#print(users)
#print(boxes)
#print(userboxes)

def userlist():
    return users

def userlistuser():
    return users   

def userlistadd(user):
    users.append(user)
    pdata.write(users,'users')
    return
    
    for i in range(len(userboxes)):
        userlist1.append('/'+userboxes[i][0])
    return userlist1

def userappend(user):
    users = []
    users=pdata.read(users,'users')
    #print(users)
    users.append(user)
    pdata.write(users,'users')
    print(users)
    return 

def usersupdate(users):
    users=[]
    users=pdata.read(users,'users')
    
def userremove(user):
    users = []
    users=pdata.read(users,'users')
    print(users)
    if users.count(user)>0:
        users.remove(user)
        pdata.write(users,'users')
        print(users)
    return 


def boxuserlist(username):
    boxlist1=[]
    for i in range(len(userboxes)):
        if userboxes[i][0]==username:
            for j in range(len(userboxes[i])):
                roomlist1.append(userboxes[i][j])
    if boxlist1:
        del boxlist1[0]
        del boxlist1[0]
    return boxlist1   

def boxlist():
    return boxes

def menulevel(state=''):
    global ml
    if state=='пользователи':
        ml='пользователями' 
    if state=='боксы':
        ml='боксами' 
    menulevel=ml
    return menulevel

def inputtext(text):
    global inputtextstr
    inputtextstr=text
    return inputtextstr
