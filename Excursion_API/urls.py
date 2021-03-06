"""Excursion_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#FOR THE FIRST VERSION
#from django.contrib import admin
#from django.urls import path,include
#from rest_framework import routers
#from EXapps import views
#router=routers.DefaultRouter()
#router.register(r'posts',views.APIDataView,'Excursion_API')

from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('EXapps.urls')),

    #path to djoser endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]
