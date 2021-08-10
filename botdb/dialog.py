import airtable
import airdata
messagelist=airdata.getairdata()
def answer():
    print('вопрос')
def question():
    print('ответ')
    
def dialog(text):
    dialog="Принято"
    messagelist=airdata.getairdata()
    for i in range(len(messagelist)):
        #print(messagelist[i][0],messagelist[i][1])
        if text==messagelist[i][0]:
            dialog=messagelist[i][1]
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