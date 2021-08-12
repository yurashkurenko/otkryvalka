import airtable
import airdata
messagelist=airdata.getairdata()
def answer():
    print('вопрос')
def question():
    print('ответ')
    
def dialog(text):
#    dialog=[]
#    dialog.append(text+" Ок")
#    dialog.append("['Клавиатура']")
#    dialog.append('команда')
    messagelist=airdata.getairdata()
    # dialog=[]
    # dialog.append(text+messagelist[0][1])
    # dialog.append(messagelist[0][2])
    # dialog.append(messagelist[0][3])
    for i in range(len(messagelist)):
        #print(messagelist[i][0],messagelist[i][1])
        if i==0:
            dialog=[]
            dialog.append(text+messagelist[0][1])
            dialog.append(messagelist[0][2])
            dialog.append(messagelist[0][3])
        if text==messagelist[i][0]:
            dialog=[]
            dialog.append(messagelist[i][1])
            dialog.append(messagelist[i][2])
            dialog.append(messagelist[i][3])
            print(text,dialog)
    return dialog
    
# def dialog1(text):
    # dialog=text
    # if text=='Привет':
        # dialog='Добрый день'
    # if text=="Пользователи":
        # dialog='Пользователей очень много, не влезут на экран...'
    # if text=="Боксы":
        # dialog='Управление боксами...'
    # return dialog