# Generated by Django 4.2.2 on 2023-06-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_amazon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='item_img',
            field=models.ImageField(upload_to='../item_pictures/'),
        ),
    ]
