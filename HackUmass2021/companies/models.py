from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from Users.models import User

# Create your models here.

class UserGraphPoint(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=40)
    info = models.CharField(max_length=1000)

class Graph(models.Model):
    company = models.OneToOneField(Company, on_delete=CASCADE)
    users = models.ManyToManyField(User)