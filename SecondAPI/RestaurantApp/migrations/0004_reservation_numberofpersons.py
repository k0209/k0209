# Generated by Django 3.2.5 on 2021-07-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantApp', '0003_reservation_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='Numberofpersons',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
