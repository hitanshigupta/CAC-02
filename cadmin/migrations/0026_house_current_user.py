# Generated by Django 4.2.5 on 2024-01-31 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadmin', '0025_staff_details_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='current_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_user', to=settings.AUTH_USER_MODEL),
        ),
    ]