# Generated by Django 4.1 on 2022-08-17 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='test',
        ),
    ]
