# Generated by Django 3.2.5 on 2022-07-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20220701_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
