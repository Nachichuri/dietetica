from django.db import models

class HomeInfo(models.Model):
    store_name = models.CharField(max_length=50)
    main_title = models.CharField(max_length=100)
    main_description = models.TextField()
    main_image = models.ImageField(upload_to='main/images')
    gluten_free_logo = models.ImageField(upload_to='main/logos')
    vegan_logo = models.ImageField(upload_to='main/logos')
    natural_logo = models.ImageField(upload_to='main/logos')
    organic_logo = models.ImageField(upload_to='main/logos')
    products_title = models.CharField(max_length=100)
    products_description = models.TextField()
    recipe_title = models.CharField(max_length=50)
    recipe_description = models.TextField()
    hours_oneline = models.CharField(max_length=100)
    hours_weekdays_morning = models.CharField(max_length=50)
    hours_weekdays_evening = models.CharField(max_length=50)
    hours_weekdays = models.CharField(max_length=50)

    def __str__(self):
        return self.store_name


class ContactInfo(models.Model):
    store_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    facebook_page = models.CharField(max_length=100)
    instagram_page = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name


class MainCategories(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main/images')
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main/images')
    description = models.TextField()

    def __str__(self):
        return self.title