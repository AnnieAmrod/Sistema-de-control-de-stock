# Generated by Django 3.2 on 2023-10-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockManagementApp', '0006_auto_20231009_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='fecha_caducidad',
            field=models.DateField(blank=True, null=True),
        ),
    ]