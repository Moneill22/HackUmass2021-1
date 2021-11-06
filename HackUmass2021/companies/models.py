from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from Users.models import User
import uuid

# Create your models here.

class UserGraphPoint(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)


class Company(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40, unique=True)
    info = models.CharField(max_length=1000)

class Graph(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.CharField(unique=True)
    users = models.ManyToManyField(User)