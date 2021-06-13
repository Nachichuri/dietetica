from django.db import models

class HomeInfo(models.Model):
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='main/images')

    def __str__(self):
        return self.title

class MainCategories(models.Model):
    name = mordels.CharField(max_length=100)
    image = models.ImageField(upload_to='main/images')

    def __str__(self):
        return self.title

class Product(models.Model):
    name = mordels.CharField(max_length=100)
    image = models.ImageField(upload_to='main/images')

    def __str__(self):
        return self.title