# Generated by Django 4.1.5 on 2023-01-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='url_site',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
