# Generated by Django 4.1.2 on 2022-10-20 12:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publishment', models.CharField(blank=True, max_length=255)),
                ('translator', models.CharField(blank=True, max_length=255)),
                ('publish_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1800), django.core.validators.MaxValueValidator(2020)])),
            ],
        ),
    ]
