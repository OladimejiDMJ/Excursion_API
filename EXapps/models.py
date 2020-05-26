from django.db import models
class APIData(models.Model):
	id=models.CharField(primary_key=True,max_length=12)
	name=models.CharField(max_length=50)
	detailPageName=models.CharField(max_length=200)
	portID=models.CharField(max_length=20)
	type=models.CharField(max_length=20)
	typology=models.CharField(max_length=20)
	activityLevel=models.CharField(max_length=50)
	collectionType=models.CharField(max_length=200)
	duration=models.CharField(max_length=200)
	language=models.CharField(max_length=50)
	pricelevel=models.IntegerField()
	currency=models.CharField(max_length=10)
	mealInfo=models.CharField(max_length=10,blank=True)
	status=models.CharField(max_length=50)
	shortDescription=models.CharField(max_length=10,blank=True)
	longDescription=models.TextField()
	externalContent=models.BooleanField(default=True)
	minimumAge=models.CharField(max_length=10,blank=True)
	wheelChairAccessible=models.BooleanField()
	featured=models.BooleanField()
	def __str__(self):
	 """A string representation of the model.""" 
	 return self.name
# Create your models here.
