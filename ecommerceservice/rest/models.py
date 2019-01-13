from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.IntegerField
    description = models.TextField
    # availableSizes = models.IntegerField(default=0)



