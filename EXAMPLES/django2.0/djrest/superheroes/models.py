"""
Models for the Superhero database. Contains all data necessary for the API
"""

from django.db import models
from datetime import date

class Power(models.Model):
    """
    A superpower. May be attached to either a Superhero or an Enemy. Name should be short and
    distinctive. Description can be verbose.
    """
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class DefaultDate(models.DateField):

    def from_db_value(self, value, expression, connection, context):
        """
        Overwrite predefined name from_db_value

        :param value:
        :param expression:
        :param connection:
        :param context:
        :return:
        """
        if value is None:
            value = date.today()
        return value

class City(models.Model):
    """
    One city. This is the main base city of the superhero.
    """
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        """
        :return: Pretty version of the City object
        """
        return self.name

class Enemy(models.Model):
    """
    An enemy of a Superhero -- typically a supervillain.
    """
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    class Meta:
        permissions = [('create_dataframe', 'Can Create Dataframe')]

    def __str__(self):
        return self.name

class Superhero(models.Model):
    """
    A hero with super powers. Like the rest of us, but better in every way.
    """
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32)
    date_of_death = DefaultDate(null=True)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return self.name


