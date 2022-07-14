# Generated by Django 3.1.5 on 2022-06-10 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220610_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='series',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='series',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.series', verbose_name='Series'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='slug',
            field=models.CharField(default=0, max_length=200),
        ),
    ]