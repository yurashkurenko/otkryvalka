import requests
all=['9003','1002','1003','2001','2002','2003','2004','3001','3002','3003','3004','4001','4002','4003']
server='192.168.1.60:8080'
#roomkey='h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz'
#response=requests.get('http://82.146.54.116:8080/lOZID_NzdLlF1oSx99GznhAr_I6eBuR3/get/V0')
##http://blynk-cloud.com/auth_token/update/pin?value=value
roomkey={'9003': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '1002': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '1003': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2001': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2002': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2003': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2004': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3001': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3002': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3003': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3004': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '4001': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '4002': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '4003': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz'}

select_room='9003'
#resptext='http://'+server+'/'+roomkey.get(select_room)+'/'

def door_check(select_room):
    block_resp='http://'+server+'/'+roomkey.get(select_room)+'/get/V0'
    response_block=requests.get(block_resp)

    check_block=response_block.text[2]
#   print(response.text)
    
    if check_block=='1':
        checkmessage1='Замок разблокирован.'
    else:
        checkmessage1='Замок заблокирован.'
    
    open_resp='http://'+server+'/'+roomkey.get(select_room)+'/get/V1'
    response_open=requests.get(open_resp)
    check_open=response_open.text[2]
    
    if check_open=='0':
        checkmessage2='Дверь открыта'
    else:
        checkmessage2='Дверь закрыта'
    
    checkmessage="Комната "+select_room+", "+checkmessage2+", "+checkmessage1
    print(checkmessage)
    return checkmessage
   

def door_block(select_room):
     t_resp='http://'+server+'/'+roomkey.get(select_room)+'/update/V9?value="1"'
     print(t_resp)
     response=requests.get(t_resp)
     checkmessage=door_check(select_room)
     return checkmessage
     

def door_unblock(select_room):
     t_resp='http://'+server+'/'+roomkey.get(select_room)+'/update/V8?value=1'
     print(t_resp)
     response=requests.get(t_resp)
     checkmessage=door_check(select_room)
     return checkmessage
#     bot.send_message(message.chat.id, checkmessage, reply_markup=gen_markup())
#select_room='3003'
#print(select_room+' '+roomkey.get(select_room))
#select_room='4003'
#print(select_room+' '+roomkey.get(select_room))