# Generated by Django 4.0.10 on 2023-05-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_sectorcoin_coinrequest_status_coinrequest_sector'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinrequest',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='coinrequest',
            name='testField',
        ),
        migrations.AlterField(
            model_name='coinrequest',
            name='description',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='coinrequest',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='coinrequest',
            name='status',
            field=models.CharField(choices=[('p', 'pending'), ('d', 'done')], default='p', max_length=1),
        ),
        migrations.DeleteModel(
            name='SectorCoin',
        ),
        migrations.DeleteModel(
            name='TestCoins',
        ),
    ]