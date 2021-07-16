# Generated by Django 3.2.5 on 2021-07-15 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('Emp', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('DateOfJoining', models.DateField()),
                ('PhotoFileName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('ReservationDayId', models.AutoField(primary_key=True, serialize=False)),
                ('ReservationHourId', models.CharField(max_length=100)),
                ('NameId', models.CharField(max_length=50)),
            ],
        ),
    ]
