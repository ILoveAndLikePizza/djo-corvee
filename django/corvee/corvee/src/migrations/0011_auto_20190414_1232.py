# Generated by Django 2.2 on 2019-04-14 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0010_auto_20190414_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persoon',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name_plural': 'Personen'},
        ),
    ]
