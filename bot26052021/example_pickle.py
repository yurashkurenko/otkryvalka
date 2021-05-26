#  example_pickle
import pdata
boxes=['/13o1','/1o2','/1o3','/2o1','/2o2','/2o3','/2o4','/3o2','/3o3','/3o4','/4o1','/4o2','/4o3']
print(boxes)
pdata.write(boxes,'boxes')
newbox=[]
newbox=pdata.read(newbox,'boxes')
print(newbox)
