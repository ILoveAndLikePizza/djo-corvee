# Generated by Django 2.2 on 2019-04-14 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_auto_20190414_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persoon',
            name='latest',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
