from django.db import models

# Create your models here.


class User(models.Model):
	GPA = models.DecimalField(decimal_places = 3, max_digits = 10)
	NUMBER_OF_INTERNSHIPS = models.IntegerField()
	DEGREE = models.BooleanField(default = False)
	college = models.TextField(blank = True, null = True)
	CODING_INTERVIEW_SKILL = models.DecimalField(decimal_places = 3, max_digits = 10)
	PROJECTS = models.BooleanField(default = False)