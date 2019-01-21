from django.db import models
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()

class Ingredient(models.Model):
    vitamin_type = models.TextField()
    vitamin_name = models.TextField()
    description = models.TextField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

