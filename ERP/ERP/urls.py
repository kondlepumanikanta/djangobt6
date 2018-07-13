"""ERP URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
#def func1(request):
#	return HttpResponse("sales")
#def func2(request):
	#return HttpResponse("purchase")
#def func3(request):
	#return HttpResponse("warehouse")
#def func4(request):
	#return HttpResponse("stock")
#def func5(request):
	#return HttpResponse("product")

from sales.views import func1,func01,func001
from purchase.views import func2,func02,func002
from warehouse.views import func3,func03,func003
from stock.views import func4,func04,func004
from product.views import func5,func05,func005
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gotosales/', func1),
    url(r'^gotohtml/', func01),
    url(r'^gototemplate/', func001),
    url(r'^gotopurchase/', func2),
    url(r'^gotohtml2/', func02),
    url(r'^gototemplate/', func002),
    url(r'^gotowarehouse/', func3),
    url(r'^gotohtml3/', func03),
    url(r'^gototemplate/', func003),
    url(r'^gotostock/', func4),
    url(r'^gotohtml4/', func04),
    url(r'^gototemplate/', func004),
    url(r'^gotoproduct/', func5),
    url(r'^gotohtml5/', func05),
    url(r'^gototemplate/', func005),
    
]
