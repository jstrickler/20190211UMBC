from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name

