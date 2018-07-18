"""studyspace URL Configuration

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
from app2.views import view_index, view_syudyhalls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gotohtml/', view_index),
    url(r'^studyhalls/', view_syudyhalls),
]
'''from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from app2.views import view_studyhall

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',view_studyhall),

    #url(r'^studyhall/',studyhall),
    #url(r'^enquire/',enquire),
    #url(r'^expense/',expense),
]
'''