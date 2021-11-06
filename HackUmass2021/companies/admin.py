from django.contrib import admin
from django.db import models
from . import models

# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Graph)
