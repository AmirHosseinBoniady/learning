# Generated by Django 4.1.2 on 2022-10-27 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('property', models.IntegerField()),
                ('nationality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('year', models.DateField()),
                ('color', models.CharField(max_length=255)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Amir.brand')),
            ],
        ),
    ]
