# Generated by Django 4.2.7 on 2024-01-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0006_alter_usertype_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_details',
            name='staff_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
