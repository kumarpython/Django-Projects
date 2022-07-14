# Generated by Django 3.1.5 on 2022-06-11 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20220611_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='series_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.category'),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tseries',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.series'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='published',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]