from testapp.models import CarBrands,CarModels
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from carapi1.forms import CarBrandForm
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from carapi1.mixins import SerializeMixin
def get_brands_data(request):
    cbrands=CarBrands.objects.all()
    jdata=serializers.serialize('json',cbrands)
    pdata=json.loads(jdata)
    print('@@pdata',pdata)
    list_data=[]
    for data in pdata:
        print('@@data',data)
        odata=data['fields']
        list_data.append(odata)
    print('@@list_data',list_data)
    dict_data={'qs':list_data}
    print('@@dict_data',dict_data)
    return JsonResponse(dict_data)
@csrf_exempt
def insert_brand_data(request):
    body=request.body
    try:
        data=json.loads(body)
        jdata=True
    except:
        jdata=False
    if jdata==True:
        if request.method=='POST':
            form=CarBrandForm(data=data)
            if form.is_valid():
                form.save(commit=True)
                return JsonResponse({'msg':'record inserted successfully...'})
            if form.errors:
                return JsonResponse(form.errors)
        return JsonResponse({'msg':'please provide post request....'})
    return JsonResponse({'msg':'please provide valid json...'})
@csrf_exempt
def update_brand_data(request,id):
        print('@@@id',id)
        if request.method=='POST':
            body=request.body

            try:
                bdata=json.loads(body)
                jdata=True
            except:
                jdata=False
            if jdata==True:
                #id=bdata.get("id",None)
                print('@@id',id)
                if id!=None:
                    try:
                        qs=CarBrands.objects.get(id=id)
                    except CarBrands.DoesNotExist:
                        return JsonResponse({'msg':'no records found for this id..'})
                    sdata=SerializeMixin.serialize_qs_data(data=[qs,])
                    print('@@@sdata',sdata)
                    for data in sdata:
                        print('@@data',data)
                        pdata=data
                        print('@@beforeupdate',pdata)
                        pdata.update(bdata)
                        print('@@@updateddata',pdata)
                        form=CarBrandForm(data=pdata,instance=qs)
                        if form.is_valid():
                            form.save(commit=True)
                            return JsonResponse({'msg':'record updated successfully..'})
                        if form.errors:
                            return JsonResponse(form.errors)
                return JsonResponse({'msg':'please provide id to update the data..'})
        return JsonResponse({'msg':'please provide POST request...'})
def delete_brand_data(request,id):
    try:
        qs=CarBrands.objects.get(id=id)
        data=qs.delete()
        print('@@deleteddata',data)
        return JsonResponse({'msg':'record deleted successfully..'})
    except CarBrands.DoesNotExist:
        return JsonResponse({'msg':'no records found for this id..'})
