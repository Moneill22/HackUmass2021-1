from django.db import models

# Create your models here.


class Graph(models.Model):
    pass
class Company(models.Model):
    name = models.CharField(max_length=40)
    info = models.CharField(max_length=1000)
    # graph = models.OneToOneField(Graph)
