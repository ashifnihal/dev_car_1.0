from django.contrib import admin
from testapp.models import CarBrands,CarModels,SpareParts
class CarBrandAdmin(admin.ModelAdmin):
    list_display=['id','brand','country']
admin.site.register(CarBrands,CarBrandAdmin)
class CarModelAdmin(admin.ModelAdmin):
    list_display=['id','brand','model','year','type','fuel','price']
admin.site.register(CarModels,CarModelAdmin)
class SparePartsAdmin(admin.ModelAdmin):
    list_display=['id','model','spoiler','wheels','brakes','headlamps','taillamps','airbags','clutchplates']
admin.site.register(SpareParts,SparePartsAdmin)
# Register your models here.
