# Generated by Django 5.0.4 on 2024-04-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_businfo_is_running'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businfo',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=19),
        ),
        migrations.AlterField(
            model_name='businfo',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=19),
        ),
    ]
