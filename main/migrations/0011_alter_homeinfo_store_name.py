# Generated by Django 3.2.4 on 2021-06-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_homeinfo_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeinfo',
            name='store_name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
    ]
