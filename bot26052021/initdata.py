import pdata
rooms=['13o1','1o2','1o3','2o1','2o2','2o3','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3']
pdata.write(rooms,'rooms')
roomkey={'13o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '1o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '1o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '2o4': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '3o4': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '4o1': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '4o2': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz',
         '4o3': 'h9pbfxfFXBsjEflpfLaB1FrQw1wjbOIz'}
pdata.write(roomkey,'roomkey')
users=['@yurasof1t1972','Adigeysha','yurasoft19721','yurasoft1972','sultanice','Btctrader']
pdata.write(users,'users')
userroom=[['@yurasof1t1972','admin','13o1','1o2','1o3','2o1','2o2','2o3','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3'],
['Adigeysha','user','13o1','1o2','1o3','2o1','2o2','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3'],
['yurasoft19721','user','1o2','1o3','2o1','2o2','2o3','2o4','3o1'],
['yurasoft1972','user','1o2'],
['sultanice','user','13o1','1o2','1o3','3o2','3o3','3o4','4o1','4o2','4o3'],
['Btctrader','user','13o1','1o2','1o3','3o2','3o3','3o4','4o1','4o2','4o3']]
pdata.write(userroom,'userroom')
userboxes=[['@yurasof1t1972','admin','13o1','1o2','1o3','2o1','2o2','2o3','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3'],
['Adigeysha','user','13o1','1o2','1o3','2o1','2o2','2o4','3o1','3o2','3o3','3o4','4o1','4o2','4o3'],
['yurasoft19721','user','1o2','1o3','2o1','2o2','2o3','2o4','3o1'],
['yurasoft1972','user','1o2'],
['sultanice','user','13o1','1o2','1o3','3o2','3o3','3o4','4o1','4o2','4o3'],
['Btctrader','user','13o1','1o2','1o3','3o2','3o3','3o4','4o1','4o2','4o3']]
pdata.write(userboxes,'userboxes')