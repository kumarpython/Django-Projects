# Generated by Django 3.1.5 on 2022-06-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220610_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='series',
            name='series_summary',
            field=models.TextField(),
        ),
    ]
