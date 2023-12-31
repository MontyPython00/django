# Generated by Django 4.0.10 on 2023-05-14 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCoins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CoinRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('testField', models.ManyToManyField(to='market.testcoins')),
            ],
        ),
    ]
