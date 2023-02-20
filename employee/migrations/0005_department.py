# Generated by Django 4.1.6 on 2023-02-20 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employee_barangay_employee_city_employee_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'department',
            },
        ),
    ]
