# Generated by Django 3.2 on 2021-05-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0003_auto_20210503_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile',
            field=models.ImageField(default='default.jpg', upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='products'),
        ),
    ]
