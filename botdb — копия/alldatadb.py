import db
levelbuffer=[]


def userlist():
    userlist1=''
    users=[]
    users=db.fetchall('users',['user'])
    for j in range(len(users)):
        userlist1=userlist1+' /'+list(users[j].values())[0]
    return userlist1
    
def boxlist():
    boxlist1=''
    boxes=[]
    boxes=db.fetchall('boxes',['box'])
    for j in range(len(boxes)):
        boxlist1=boxlist1+' /'+list(boxes[j].values())[0]
    return boxlist1
    
def boxlistlist():
    boxes=[]
    boxes=db.fetchall('boxes',['box'])
    return boxes    

def menulevel(state=''):
    if state!="":
        db.updateml(state)
    ml=[]
    ml=db.fetchall('menulevel',['ml'])
    menulevel=(list(ml[0].values())[0])
    return menulevel
    
def messagestringbuffer(message=''):
    if message!='':
        db.updatemsb(message)
    msb=[]
    msb=db.fetchall('messagestringbuffer',['message'])
    message1=(list(msb[0].values())[0])
    return message1

def inputtext(text):
    return text
    
def buttonlist(state):
    buttontoople=db.fetchcelltext('botstate','keyboard',state)
    buttonstring=buttontoople[0]
    buttonlist=[]
    buttonlist=buttonstring.split(' ')
    return buttonlist
    
def message(state):
    messagetoople=db.fetchcelltext('botstate','message',state)
    messagestring=messagetoople[0]
    return messagestring 

def command(state):
    commandtoople1=db.fetchcelltext('botstate','level1',state)
    commandtoople2=db.fetchcelltext('botstate','level2',state)
    commandstring=commandtoople1[0]+' '+commandtoople2[0]
    return commandstring
    
def commandlv1(state):
    commandtoople1=db.fetchcelltext('botstate','level1',state)
    commandstring=commandtoople1[0]
    return commandstring
    
def commandlv2(state):
    commandtoople2=db.fetchcelltext('botstate','level2',state)
    commandstring=commandtoople2[0]
    return commandstring

def commandlv3(state):
    commandtoople3=db.fetchcelltext('botstate','level3',state)
    commandstring=commandtoople3[0]
    return commandstring
    
def commandlv4(state):
    commandtoople4=db.fetchcelltext('botstate','level4',state)
    commandstring=commandtoople4[0]
    return commandstring

def insertuser(user):
    db.insert('users',{'user':user})
    return
    
def deleteuser(user):
    iddelete=db.fetchidforusers(user)
    for i in range(len(iddelete)):
        db.delete('users',iddelete[i])
    return
    
def insertbox(box):
    api=''
    users=''
    db.insert('boxes',{'box':box,'api':api,'users':users})
    return
    
def deletebox(box):
    iddelete=db.fetchidforboxes(box)
    for i in range(len(iddelete)):
        db.delete('boxes',iddelete[i])
    return
    
def insertboxuser(box,user):
    listusers=db.getlistuserforbox(box)
    listusers=listusers+' '+user
    db.setlistuserforbox(box,listusers)
    return
    
def deleteboxuser(box,user):
    strusers=db.getlistuserforbox(box)
    listusers=[]
    listusers=strusers.split(' ')
    for i in range(len(listusers)):
        if listusers.count(user)>0:
            listusers.remove(user)
    strusers=' '.join(listusers)
    db.setlistuserforbox(box,strusers)
    return
    
def listboxusers(box):
    listusers=db.getlistuserforbox(box)
    return listusers
    
def selectbox(box=''):
    if box!='':
        db.updateselectedbox(box)
    box=[]
    box=db.fetchall('selectedboxusers',['box'])
    box=(list(box[0].values())[0])
    return box
   
def selectuser(user=''):
    if user!='':
        db.updateselecteduser(user)
    user=[]
    user=db.fetchall('selectedboxusers',['user'])
    user=(list(user[0].values())[0])
    return user