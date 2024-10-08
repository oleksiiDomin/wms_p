# Generated by Django 4.2.15 on 2024-09-01 09:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wms_app', '0009_order_coil_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetalShot',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wms_app.material')),
                ('diameter', models.FloatField(validators=[django.core.validators.MaxValueValidator(3.0), django.core.validators.MinValueValidator(3.0)])),
            ],
            bases=('wms_app.material',),
        ),
        migrations.CreateModel(
            name='MetalStrip',
            fields=[
                ('material_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wms_app.material')),
                ('thickness', models.FloatField(validators=[django.core.validators.MaxValueValidator(1.0), django.core.validators.MinValueValidator(0.1)])),
                ('width', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MaxValueValidator(30)])),
            ],
            bases=('wms_app.material',),
        ),
        migrations.AlterField(
            model_name='carbon',
            name='carbon_p',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(100.0)]),
        ),
        migrations.AlterField(
            model_name='carbon',
            name='sulfur_p',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]
