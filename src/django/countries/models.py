from djongo import models
# from django.db import models
from django.db.models.query_utils import select_related_descend

# Create your models here.


class Country(models.Model):
    id = models.TextField(primary_key=True)
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    flag = models.Tename = models.TextField()
    area = models.FloatField()

    def __str__(self):
        return self.name


class Covid_Cases(models.Model):
    id = models.TextField(primary_key=True)
    country_name = models.CharField(max_length=255)
    total_cases = models.IntegerField()
    new_cases = models.IntegerField()
    total_deaths = models.IntegerField()

    def __str__(self):
        return self.country_name
