# Generated by Django 4.0.4 on 2022-05-04 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_seats_alter_bookedseat_seat_delete_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentIntent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer', models.URLField()),
                ('movie_title', models.CharField(max_length=255)),
                ('seat_number', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
                ('occupant_first_name', models.CharField(max_length=255)),
                ('occupant_last_name', models.CharField(max_length=255)),
                ('occupant_email', models.EmailField(max_length=555)),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('seat_no', models.IntegerField()),
                ('movie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieBooked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('booked_seats', models.ManyToManyField(blank=True, to='booking.seat')),
            ],
        ),
    ]
