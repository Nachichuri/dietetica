from django.db import models
from django.utils.text import slugify
from django.db.models.deletion import SET_NULL

class HomeInfo(models.Model):
    store_name = models.CharField(max_length=50)
    main_title = models.CharField(max_length=100)
    main_description = models.TextField()
    main_image = models.ImageField(upload_to='main/images', null=True, blank=True)
    gluten_free_logo = models.FileField(upload_to='main/logos', null=True, blank=True)
    gluten_free_message = models.CharField(max_length=100, null=True, blank=True, default='')
    vegan_logo = models.FileField(upload_to='main/logos', null=True, blank=True)
    vegan_message = models.CharField(max_length=100, null=True, blank=True, default='')
    natural_logo = models.FileField(upload_to='main/logos', null=True, blank=True)
    natural_message = models.CharField(max_length=100, null=True, blank=True, default='')
    organic_logo = models.FileField(upload_to='main/logos', null=True, blank=True)
    organic_message = models.CharField(max_length=100, null=True, blank=True, default='')
    products_title = models.CharField(max_length=100)
    products_description = models.TextField()
    recipe_title = models.CharField(max_length=50)
    recipe_description = models.TextField()
    hours_oneline = models.CharField(max_length=100)
    hours_weekdays_morning = models.CharField(max_length=50, null=True, blank=True)
    hours_weekdays_evening = models.CharField(max_length=50, null=True, blank=True)
    hours_weekends = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.store_name


class ContactInfo(models.Model):
    store_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    facebook_page = models.CharField(max_length=100, null=True, blank=True)
    instagram_page = models.CharField(max_length=100, null=True, blank=True)
    whatsapp_link = models.CharField(max_length=100, null=True, blank=True)
    googlemaps_link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.store_name


class MainCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False, primary_key=True)
    image = models.ImageField(upload_to='main/images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MainCategory, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False, primary_key=True)
    category = models.ForeignKey(MainCategory, on_delete=SET_NULL, null=True)
    image = models.ImageField(upload_to='main/images', null=True, blank=True)
    properties = models.TextField(null=True, blank=True)
    usage = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)  

    def __str__(self):
        return self.name