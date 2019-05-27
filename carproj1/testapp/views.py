from django.shortcuts import render
from testapp.models import CarBrands,CarModels,SpareParts,Register
from django.http import HttpResponse,JsonResponse
from testapp.forms import CarDetailForm,SparePartsForm,CarBrandsForm,RegisterForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register1(request):
     form=RegisterForm()
     # print('@@form',form)
     if request.method=='POST':
         form=RegisterForm(request.POST)
         if form.is_valid():
             firstname=form.cleaned_data['first_name']
             lastname=form.cleaned_data['last_name']
             email=form.cleaned_data['email']
             username=form.cleaned_data['username']
             password=form.cleaned_data['password']
             print('@firstname',firstname,'@lastname',lastname,'@email',email,'password',password)
             try:
                 user=form.save()
                 user.set_password(user.password)
                 user.save()
                 return HttpResponse('user registered successfully...')
             except form.errors:
                    print('@@@@error',form.errors)

     return render(request,'testapp/register.html',context={'form':form})
@csrf_exempt
def login1(request,backend='django.contrib.auth.backends.ModelBackend'):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        return form
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print('@@username',username,'@@password',password)
            try:
                data=Register.objects.get(email=username)
                rusername=data.email
                rpassword=data.passord1
                print('@@rusername',rusername,'@@rpassword',rpassword)
                if str(username)==str(rusername):
                    if str(password)==str(rpassword):
                        return render(request,'testapp/home.html')
                    else:
                        print(password,'@@please provide valid password')
                else:
                    print(username,'@@username please provide valid username')
            except Register.DoesNotExist:
                print('no record found by using that username..')
    return render(request,'testapp/login.html',context={'form':form})

@csrf_exempt
def get_home(request):
    return render(request,'testapp/home.html')
def get_car_brand_details(request):
    data=CarBrands.objects.all()
    return render(request,'testapp/carbrands.html',context={'cdata':data})
def get_car_details_by_brand(request):
    brandid=request.GET.get('brandid',None)
    print('@@brandid',brandid)
    if brandid!=None:
        try:
            data=CarModels.objects.filter(brand_id=brandid)
            return render(request,'testapp/cardetails.html',context={'cdata':data})
        except CarModels.DoesNotExist:
            return HttpResponse('no records found for this id..')
    return HttpResponse('please provide brand to get details...')

@csrf_exempt
@login_required
def insert_carbrand_data(request):
    form=CarBrandsForm()
    if request.method=='POST':
        form=CarBrandsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return JsonResponse({'msg':'record inserted successfully...'})
    return render(request,'testapp/insertcarbranddata.html',context={'form':form})

@login_required
def insert_car_data(request):
    form=CarDetailForm()
    if request.method=="POST":
        form=CarDetailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('record inserted successfully')
        if form.errors:
            print('@@form.errors',form.errors)
            return HttpResponse(form.errors)

    return render(request,'testapp/insertcardetails.html',context={'form':form})
@login_required
def update_car_data(request):
    id=request.GET.get('id',None)
    if id!=None:
        qs=CarModels.objects.get(id=id)
        qdata={'brand':qs.brand,'model':qs.model,'year':qs.year,'type':qs.type,'price':qs.price}
        print('@@qdata',qdata)
        if request.method=='POST':
            form=CarDetailForm(request.POST,instance=qs)
            print('@@form',form)
            if form.is_valid():
                print('form is valid....')
                form.save()
                return HttpResponse('record updated successfully...')
            if form.errors:
                print('@@form.errors',form.errors)
                return HttpResponse(form.errors)
        return render(request,'testapp/updatecardetails.html',context={'qdata':qs})
    return HttpResponse('please provide id to update data')
def view_spare_parts(request):
    model_id=request.GET.get('model_id',None)
    if model_id!=None:
        sdata=SpareParts.objects.filter(model_id=model_id)
        return render(request,'testapp/sparepartsdetails.html',context={'sdata':sdata})
    return HttpResponse('please provide model_id to get the data...')
@login_required
def insert_sparepart_data(request):
    form=SparePartsForm()
    if request.method=='POST':
        form=SparePartsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('record inserted successfully...')
    return render(request,'testapp/insertsparepartdata.html',context={'form':form})
@login_required
def update_sparepart_data(request):
    id=request.GET.get('id',None)
    if id!=None:
        qdata=SpareParts.objects.get(id=id)
        if request.method=='POST':
            form=SparePartsForm(request.POST,instance=qdata)
            if form.is_valid():
                form.save()
                return HttpResponse('record updated successfully...')
        return render(request,'testapp/updatesparepartdata.html',context={'qdata':qdata})
    return HttpResponse('please provide id to get the record details..')
@login_required
def delete_sparepartdata(request):
    id=request.GET.get('id',None)
    if id!=None:
        qdata=SpareParts.objects.get(id=id)
        ddata=qdata.delete()
        print('@@ddata',ddata)
        return HttpResponse('record deleted successfully..')
    return HttpResponse('please provide id to get the record details..')



# Create your views here.
