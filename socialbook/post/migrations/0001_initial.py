# Generated by Django 3.2.5 on 2022-07-28 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50)),
                ('text', models.TextField(max_length=100)),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(blank=True)),
                ('approved', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='group_pic')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post_image')),
                ('tags', models.CharField(max_length=20)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
    ]
