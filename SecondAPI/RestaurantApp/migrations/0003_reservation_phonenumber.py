# Generated by Django 3.2.5 on 2021-07-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0002_auto_20210715_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Phonenumber',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]