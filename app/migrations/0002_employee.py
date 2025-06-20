# Generated by Django 5.2.1 on 2025-06-16 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('age', models.CharField()),
                ('phone_no', models.CharField(max_length=10)),
                ('dept_no', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('commision', models.FloatField()),
                ('salary', models.FloatField()),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
