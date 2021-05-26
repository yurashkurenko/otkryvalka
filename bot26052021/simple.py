import blynklib
#BLYNK_AUTH = '<YourAuthToken>' #insert your Auth Token here
BLYNK_AUTH = 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz' #insert your Auth Token here
#blynk = blynklib.Blynk(BLYNK_AUTH)
blynk = blynklib.Blynk(BLYNK_AUTH,
                       server='192.168.1.60',        # set server address
                       port=8080,                       # set server port
                       #heartbeat=30,                    # set heartbeat to 30 secs
                       #log=print                       # use print function for debug logging
                       )
#blynk = BlynkLib.Blynk(BLYNK_AUTH,
#                       server='xxx.xxx.xxx.xxx',        # set server address
#                       port=8080,                       # set server port
#                       heartbeat=30,                    # set heartbeat to 30 secs
#                       #log=print                       # use print function for debug logging
#                       )

#def blockkey():
#    blynk.virtual_write(0, 1)
#    print('Заблокировано')

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


# register handler for virtual pin V4 write event
@blynk.handle_event('write V8')
def write_virtual_pin_handler(pin, value):
    blynk.virtual_write(0, 1)
#    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
#    print('Заблок2')
#    blockkey()
#    print('Заблок3')
        
@blynk.handle_event('write V9')
def write_virtual_pin_handler(pin, value):
#    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    blynk.virtual_write(0, 0)
while True:
    blynk.run()
