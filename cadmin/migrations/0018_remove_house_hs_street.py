# Generated by Django 4.2.5 on 2024-01-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0017_alter_house_street'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='hs_street',
        ),
    ]
