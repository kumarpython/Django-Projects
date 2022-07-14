# Generated by Django 3.1.5 on 2022-06-10 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220606_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tslug',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=200)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.category')),
            ],
        ),
        migrations.AddField(
            model_name='tutorial',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.series'),
        ),
    ]
