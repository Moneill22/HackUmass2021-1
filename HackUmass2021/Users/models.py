from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from companies.models import Company

# Create your models here.


class User(models.Model):
	GPA = models.DecimalField(decimal_places = 3, max_digits = 10)
	NUMBER_OF_INTERNSHIPS = models.IntegerField()
	DEGREE = models.BooleanField(default = False)
	college = models.TextField(blank = True, null = True)

	


	
class Application(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)

	company = models.IntegerField()
	response = models.IntegerField()
	
	