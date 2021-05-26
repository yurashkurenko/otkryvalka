userroom=[['@yurasof1t1972','admin','13o1','1o2','1o3','2o1','2o2','2o3','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3'],
['Adigeysha','user','13o1','1o2','1o3','2o1','2o2','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3'],
['yurasoft19721','user','1o2','1o3','2o1','2o2','2o3','2o4','3o1'],
['yurasoft1972','user','1o2'],
['sultanice','user','13o1','1o2','1o3','3o2','3o3','3o4','4o1','4o2','4o3'],
['Btctrader','user','13o1','1o2','1o3','3o2','3o3','3o4','4o1','4o2','4o3']]


boxes=['/13o1','/1o2','/1o3','/2o1','/2o2','/2o3','/2o4','/3o1','/3o2','/3o3','/3o4','/4o1','/4o2','/4o3']

def roomlist(username):
    roomlist1=[]
    for i in range(len(userroom)):
        if userroom[i][0]==username:
            for j in range(len(userroom[i])):
                roomlist1.append(userroom[i][j])
    if roomlist1:
        del roomlist1[0]
        del roomlist1[0]
    return roomlist1

def userlist():
    userlist1=[]
    for i in range(len(userroom)):
        userlist1.append('/'+userroom[i][0])
    return userlist1
    
    
def boxlist():
    return boxes