# Generated by Django 4.2.5 on 2024-01-25 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadmin', '0016_alter_house_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadmin.streets'),
        ),
    ]