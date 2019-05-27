from django.contrib import admin
from testapp.models import CarBrands,CarModels,SpareParts,Register,LoginModel
class CarBrandAdmin(admin.ModelAdmin):
    list_display=['id','brand','country']
admin.site.register(CarBrands,CarBrandAdmin)
class CarModelAdmin(admin.ModelAdmin):
    list_display=['id','brand','model','year','type','fuel','price']
admin.site.register(CarModels,CarModelAdmin)
class SparePartsAdmin(admin.ModelAdmin):
    list_display=['id','model','spoiler','wheels','brakes','headlamps','taillamps','airbags','clutchplates']
admin.site.register(SpareParts,SparePartsAdmin)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','dob','email','passord1','passord2']
admin.site.register(Register,RegisterAdmin)
class LoginAdmin(admin.ModelAdmin):
    list_display=['username','password']
admin.site.register(LoginModel,LoginAdmin)
# Register your models here.
