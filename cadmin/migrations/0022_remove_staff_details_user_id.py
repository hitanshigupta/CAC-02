# Generated by Django 4.2.5 on 2024-01-30 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0021_alter_staff_details_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_details',
            name='user_id',
        ),
    ]
