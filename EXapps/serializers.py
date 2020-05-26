from rest_framework.serializers import ModelSerializer
from . models import APIData
from rest_framework import serializers
class APIDataSerializer(serializers.ModelSerializer):
	class Meta:
		model=APIData
		fields=('name','detailPageName','typology','activityLevel','collectionType','duration','language','pricelevel','mealInfo','status','shortDescription','longDescription','externalContent','featured','id','type','typology','portID','currency','wheelChairAccessible')