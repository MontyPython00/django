# Generated by Django 4.2.2 on 2023-06-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_amazon', '0002_alter_photo_item_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='item_img',
            field=models.ImageField(upload_to='~/programming/project_amazon/backend/item_pictures/'),
        ),
    ]
