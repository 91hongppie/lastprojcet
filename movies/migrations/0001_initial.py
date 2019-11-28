# Generated by Django 2.1.1 on 2019-11-28 04:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_cd', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=150)),
                ('title_en', models.CharField(max_length=150)),
                ('audience', models.IntegerField()),
                ('summary', models.TextField(blank=True)),
                ('poster_url', models.TextField(blank=True)),
                ('backdrop_url', models.TextField(blank=True)),
                ('directors', models.CharField(blank=True, max_length=500)),
                ('release_date', models.DateField(blank=True)),
                ('actors', models.TextField(blank=True)),
                ('rate', models.CharField(blank=True, max_length=50)),
                ('running_time', models.CharField(blank=True, max_length=50)),
                ('genres', models.ManyToManyField(blank=True, related_name='movies', to='movies.Genre')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_movies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField()),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
