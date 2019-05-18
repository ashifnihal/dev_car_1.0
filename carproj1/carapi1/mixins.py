from django.core import serializers
import json
class SerializeMixin(object):
    def serialize_qs_data(data):
        jdata=serializers.serialize('json',data)
        pdata=json.loads(jdata)
        print('@@pdata',pdata)
        list_data=[]
        for data in pdata:
            print('@@data',data)
            odata=data['fields']
            list_data.append(odata)
        print('@@list_data',list_data)
        # dict_data={'qs':list_data}
        # print('@@dict_data',dict_data)
        return list_data
