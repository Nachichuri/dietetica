# Generated by Django 3.2.4 on 2021-06-19 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='main/images')),
                ('description', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='main/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.maincategory'),
        ),
        migrations.DeleteModel(
            name='MainCategories',
        ),
    ]
