# Generated by Django 4.0.4 on 2022-05-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_alter_booking_payment_type_alter_seat_seat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='seat_type',
            field=models.CharField(choices=[('', 'Select'), ('Regular', 'Regular'), ('Deluxe', 'Deluxe'), ('VIP', 'VIP')], max_length=8),
        ),
    ]
