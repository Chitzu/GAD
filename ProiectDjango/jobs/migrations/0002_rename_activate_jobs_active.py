# Generated by Django 4.1.5 on 2023-01-05 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobs',
            old_name='activate',
            new_name='active',
        ),
    ]
