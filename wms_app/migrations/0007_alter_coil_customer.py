# Generated by Django 4.2.15 on 2024-08-29 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wms_app', '0006_alter_coil_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coil',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wms_app.customer'),
        ),
    ]
