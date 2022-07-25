# Generated by Django 3.2.5 on 2022-07-25 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]