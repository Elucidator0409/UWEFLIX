# Generated by Django 4.0.4 on 2022-05-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_alter_seat_seat_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment_type',
            field=models.CharField(choices=[('Credit Card', 'Debit Card')], default='Credit Card', max_length=11),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_type',
            field=models.CharField(choices=[('', 'Select'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=8),
        ),
    ]
