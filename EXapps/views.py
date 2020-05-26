#FOR THE FIRST VERSION
#from django.shortcuts import render
#from rest_framework.mixins import(CreateModelMixin,ListModelMixin,RetrieveModelMixin,UpdateModelMixin)
#from rest_framework.viewsets import GenericViewSet
#from . models import APIData
#from . serializers import APIDataSerializer
#from rest_framework import viewsets
#class APIDataView(viewsets.ModelViewSet):
#	serializer_class=APIDataSerializer
#	queryset=APIData.objects.all()

# Create your views here.
#SECOND VERSION
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from EXapps.models import APIData 
from . serializers import APIDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET','POST','DELETE'])
def excursion_list(request):
	if request.method=='GET':
		excursion=APIData.objects.all()
		#name=request.GET.get('name',None)
		#if name is not None:
			#excursion=excursion.filter(name_icontains=name)
		excursion_serializer=APIDataSerializer(excursion,many=True)
		return Response(excursion_serializer.data) 
	elif request.method=='POST':
		excursion_data=JSONParser().parse(request)
		excursion_serializer=APIDataSerializer(data=excursion_data)
		if excursion_serializer.is_valid():
			excursion_serializer.save()
			return Response(excursion_serializer.data, status=status.HTTP_201_CREATED)
		return Response(excursion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		count=APIData.objects.all().delete()
		return JsonResponse({'message':'{} Excursion was deleted successfully'.format(count[0])},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def excursion_detail(request,pk):
	try:

		excursion=APIData.objects.get(pk=pk)
	except APIData.DoesNotExist:
		return JsonResponse(status=status.HTTP_404_NOT_FOUND)
	if request.method=='GET':
		excursion_serializer=APIDataSerializer(excursion)
		return JsonResponse(excursion_serializer.data)
	elif request.method=='PUT':
		excursion_data=JSONParser().parse(request)
		excursion_serializer=APIDataSerializer(excursion,data=excursion_data)
		if excursion_serializer.is_valid():
			excursion_serializer.save()
			return JsonResponse(excursion_serializer.data)
		return JsonResponse(excursion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method=='DELETE':
		excursion.delete()
		return JsonResponse({'message':' Excursion was deleted successfully.'},status=status.HTTP_204_NO_CONTENT)

