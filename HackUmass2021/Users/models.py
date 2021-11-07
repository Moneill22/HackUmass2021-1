from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=50, default='')
	GPA = models.DecimalField(decimal_places = 3, max_digits = 10, default=0.0)
	MONTHS_INTERNING = models.IntegerField(default = 0)
	college = models.CharField(max_length=50 ,blank = True, null = True, default='')
	
	def __str__(self) -> str:
		return self.username
	
class Application(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	company_id = models.CharField(max_length=40 ,unique=True, default='') # company name
	response = models.IntegerField()

	def __str__(self) -> str:
		return f'Application for {self.company_id}'
	