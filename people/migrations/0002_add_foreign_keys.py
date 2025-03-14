# Generated by Django 5.1.7 on 2025-03-10 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_add_country_city_citizen'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='citizens', to='people.city'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='people.country'),
        ),
    ]
