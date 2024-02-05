# Generated by Django 4.2.5 on 2024-01-30 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadmin', '0022_remove_staff_details_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_details',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]