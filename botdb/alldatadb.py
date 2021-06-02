import db

def userlist():
    userlist1=''
    users=[]
    users=db.fetchall('users',['user'])
    for j in range(len(users)):
        userlist1=userlist1+' '+list(users[j].values())[0]
    return userlist1

def menulevel(state=''):
    if state!="":
        db.updateml(state)
    ml=[]
    ml=db.fetchall('menulevel',['ml'])
    menulevel=(list(ml[0].values())[0])
    return menulevel

def inputtext(text):
    return text
    
def buttonlist(state):
    buttontupple=db.fetchcelltext('botstate','keyboard',state)
    print(buttontupple)
    buttonlist=[]
    buttonliststr=buttontupple[0]
    buttonlist=buttonliststr.split(' ')
    print(buttonlist)
    return buttonlist
    
def message(state):
    messagetupple=db.fetchcelltext('botstate','message',state)
    print(messagetupple)
    messagestr=messagetupple[0]
    print(messagestr)
    return messagestr