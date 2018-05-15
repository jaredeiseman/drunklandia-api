# Generated by Django 2.0.2 on 2018-04-27 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amenity', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Amenity',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=10)),
                ('street_one', models.CharField(max_length=255)),
                ('street_two', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.DecimalField(decimal_places=0, max_digits=5)),
                ('lat', models.DecimalField(decimal_places=10, max_digits=32)),
                ('lng', models.DecimalField(decimal_places=10, max_digits=32)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Restaurant',
            },
        ),
        migrations.CreateModel(
            name='RestaurantAmenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Amenity')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Restaurant')),
            ],
            options={
                'db_table': 'RestaurantAmenities',
            },
        ),
        migrations.CreateModel(
            name='RestaurantHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('day', models.IntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Restaurant')),
            ],
            options={
                'db_table': 'RestaurantHours',
            },
        ),
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Restaurant')),
            ],
            options={
                'db_table': 'Special',
            },
        ),
        migrations.CreateModel(
            name='SpecialHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.TimeField()),
                ('stop_time', models.TimeField()),
                ('day', models.IntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Restaurant')),
                ('special_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Special')),
            ],
            options={
                'db_table': 'SpecialHours',
            },
        ),
    ]
