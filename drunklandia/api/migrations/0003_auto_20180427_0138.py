# Generated by Django 2.0.2 on 2018-04-27 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_special_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='special',
            name='item',
            field=models.CharField(max_length=255),
        ),
    ]
