# Generated by Django 3.2.4 on 2021-06-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeinfo',
            name='recipe_image',
            field=models.ImageField(blank=True, null=True, upload_to='main/images'),
        ),
    ]