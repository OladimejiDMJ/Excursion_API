#FOR THE FIRST VERSION
#from django.urls import path
#from . import views
#urlpatterns=[
	
#	]
#THE FIRST VERSION ENDS HERE
from django.conf.urls import url
from EXapps import views
from django.urls import path
urlpatterns=[
	path('api/excursion/', views.excursion_list),
	path('api/excursion/<int:pk>/',views.excursion_detail),
	#url(r'^api/excursion',views.excursion_list),
	#url(r'api/excursion/(?<pk>[0-9]+)',views.excursion_detail),
	#url(r'^api/excursion/<int:pk>/',views.excursion_detail),

]