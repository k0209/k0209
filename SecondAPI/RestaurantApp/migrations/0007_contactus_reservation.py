# Generated by Django 3.2.5 on 2021-07-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RestaurantApp', '0006_alter_reservation_reservationid'),
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
                ('ReservationId', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ReservationDay', models.CharField(default='Today', max_length=20)),
                ('ReservationHour', models.CharField(default='9:00 PM', max_length=20)),
                ('Name', models.CharField(default='Anonymous', max_length=50)),
                ('Phonenumber', models.CharField(default='Not Disclosed', max_length=15)),
                ('Numberofpersons', models.IntegerField(default=1)),
            ],
        ),
    ]
