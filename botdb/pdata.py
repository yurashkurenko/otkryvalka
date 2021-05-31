# Для установки pickle
#pip install pickle-mixin
import pickle

def write(datap,strVarName):
#    import pickle
    with open(strVarName+'.pd', 'wb') as f:
        pickle.dump(datap, f)
    return 

def read(datap,strVarName):
#    import pickle
    with open(strVarName+'.pd', 'rb') as fn:
        datap = pickle.load(fn)
    return datap
    