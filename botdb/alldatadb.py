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
    commandtoople2=db.fetchcelltext('botstate','level2',state)
    commandstring=commandtoople1[0]+' '+commandtoople2[0]
    return commandstring