from django.db import models

class Product(models.Model):
    cost = models.IntegerField()
    name = models.CharField(max_length=20)