# Generated by Django 5.0.4 on 2024-04-20 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]
