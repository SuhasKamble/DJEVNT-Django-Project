# Generated by Django 3.0.7 on 2021-04-21 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210420_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
    ]
