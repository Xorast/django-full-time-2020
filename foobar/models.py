from django.db import models


# Create your models here.
class Movies(models.Model):
    name = models.CharField("Name", max_length=40, null=False)
    description = models.TextField("Description", max_length=200, null=False)
    time = models.CharField("Time", max_length=40, null=False)
    authors = models.CharField("Authors", max_length=40, null=False)
    realisator = models.CharField("Realisator", max_length=40, null=False)
