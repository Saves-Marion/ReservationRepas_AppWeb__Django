# Generated by Django 3.0.4 on 2020-06-01 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partage_repas', '0003_auto_20200601_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repas',
            options={'ordering': ['date'], 'verbose_name': 'repas'},
        ),
    ]