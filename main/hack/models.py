from django.db import models

# Create your models here.
class Tip (models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    start = models.DateTimeField(max_length=50)
    end = models.DateTimeField(max_length=50)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    rates = 0
    rating = 0
    comments = []
    categories = []

class Hack(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=150)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    picture = models.ImageField()
    rates = 0
    rating = 0
    comments = []
    categories = []

class Comment(models.Model):
    text = models.TextField()
    time = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
