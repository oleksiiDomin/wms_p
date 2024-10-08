# Generated by Django 4.2.15 on 2024-09-01 09:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms_app', '0010_metalshot_metalstrip_alter_carbon_carbon_p_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carbon',
            old_name='carbon_p',
            new_name='carbon_content',
        ),
        migrations.RenameField(
            model_name='carbon',
            old_name='sulfur_p',
            new_name='sulfur_content',
        ),
        migrations.AlterField(
            model_name='metalshot',
            name='diameter',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(3.0), django.core.validators.MinValueValidator(0.1)]),
        ),
        migrations.AlterField(
            model_name='metalstrip',
            name='width',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(30)]),
        ),
    ]
