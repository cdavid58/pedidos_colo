from django.db import models

class Order(models.Model):
	name_product = models.CharField(max_length = 50)
	quantity = models.IntegerField()
	
