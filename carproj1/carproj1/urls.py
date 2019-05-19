"""carproj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp.views import get_car_brand_details,get_home,get_car_details_by_brand,insert_car_data,update_car_data,view_spare_parts,insert_sparepart_data,update_sparepart_data,delete_sparepartdata,insert_carbrand_data
from carapi1 import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^getCarData/',get_car_brand_details),
    url(r'^home/',get_home),
    url(r'^cardetailsbybrand/',get_car_details_by_brand),
    url(r'^insertcarbranddata/',insert_carbrand_data),
    url(r'^insertcardata/',insert_car_data),
    url(r'^updatecardata/',update_car_data),
    url(r'^sparepartsdata/',view_spare_parts),
    url(r'^InsertSparePartData/',insert_sparepart_data),
    url(r'^updatesparepartdata/',update_sparepart_data),
    url(r'^deletesparepartdata/',delete_sparepartdata),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^api/',include('carapi1.urls')),
]
