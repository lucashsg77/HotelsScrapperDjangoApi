from django.db import models

# Create your models here.
class Hotel(models.Model):
	name = models.CharField(max_length=200)
	provider = models.CharField(max_length=200)
	rating =  models.DecimalField(max_digits=4, decimal_places=2)
	review = models.TextField()
	price = models.CharField(max_length=10)
	city = models.CharField(max_length=3)
	checkin = models.CharField(max_length=10)
	checkout = models.CharField(max_length=10)
	def __str__(self):
		return self.name