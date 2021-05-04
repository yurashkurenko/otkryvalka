import requests
all=['9003','1002','1003','2001','2002','2003','2004','3001','3002','3003','3004','4001','4002','4003']
server='192.168.1.60:8080'
room9003key='h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz'
##http://blynk-cloud.com/auth_token/update/pin?value=value
select_room=''
resptext='http://'+server+'/'+room9003key+'/'

def door_check():
    t_resp='http://'+server+'/'+room9003key+'/get/V0'
    print(t_resp)
    response=requests.get(t_resp)
#   response=requests.get('http://82.146.54.116:8080/lOZID_NzdLlF1oSx99GznhAr_I6eBuR3/get/V0')
    global checkmessage
    check123=response.text[2]
    print(response.text)
    if check123=='0':
        checkmessage='Замок заблокирован.'
    else:
        checkmessage='Замок разблокирован.'
    print(checkmessage)
    print(check123)

def door_close():
     t_resp='http://'+server+'/'+room9003key+'/update/V8?value="1"'
     print(t_resp)
     response=requests.get(t_resp)
#     response=requests.get('http://82.146.54.116:8080/lOZID_NzdLlF1oSx99GznhAr_I6eBuR3/update/V0?value=1')
     door_check()
#     bot.sendMessage(update.message.chat_id,"Вы хотите закрыть или открыть дверь? ",reply_markup)
#     bot.send_message(message.chat.id,checkmessage, reply_markup=gen_markup())
	  
#		text="Do you want to turn On or Off amplifier? " + str(stat_conv(k_amp_power.get_val())),
#		text="Вы хотите закрыть или открыть дверь? ", 
#		reply_markup=reply_markup)
def door_open():
     t_resp='http://'+server+'/'+room9003key+'/update/V9?value=1'
     print(t_resp)
     response=requests.get(t_resp)
     #response=requests.get('http://82.146.54.116:8080/lOZID_NzdLlF1oSx99GznhAr_I6eBuR3/update/V0?value=0')    
     door_check()
#     bot.send_message(message.chat.id, checkmessage, reply_markup=gen_markup())
