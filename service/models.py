from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Demand(models.Model):
	recipient = models.ForeignKey(User, on_delete=models.CASCADE)
	quantity=models.IntegerField(default=0)
	address = models.TextField(max_length=100)
	location = models.PointField(null=True,blank=True)
	
	

class Supply(models.Model):
	donor = models.ForeignKey(User, on_delete=models.CASCADE)
	address = models.TextField(max_length=100)
	donated_on = models.DateField(auto_now_add=True)
	location = models.PointField(null=True,blank=True)
	
	def get_location(self):
		pass


class DrugStock(models.Model):

	STYPE = (
		('H','Hospital'),
		('P','Pharmacy'),
		)

	name=models.CharField(max_length=30)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	address = models.TextField(blank=True,null=True)
	stocker_type = models.CharField(default=0,max_length=2,choices=STYPE) 
	location = models.PointField(null=True,blank=True)