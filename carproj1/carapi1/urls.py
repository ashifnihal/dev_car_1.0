from django.conf.urls import url,include
from django.contrib import admin
from carapi1.views import get_brands_data,insert_brand_data,update_brand_data,delete_brand_data
urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'get_brands_data_json/',get_brands_data),
url(r'insert_brand_data_json/',insert_brand_data),
url(r'update_brand_data_json/(?P<id>\d+)/',update_brand_data),
url(r'delete_brand_data_json/(?P<id>\d+)/',delete_brand_data)
]
