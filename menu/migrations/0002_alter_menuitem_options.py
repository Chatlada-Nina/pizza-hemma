# Generated by Django 4.2.19 on 2025-03-08 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['-id']},
        ),
    ]
