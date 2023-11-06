# Generated by Django 4.0.3 on 2023-11-06 20:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name': 'Žánr', 'verbose_name_plural': 'Žánry'},
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('plot', models.TextField(blank=True, null=True, verbose_name='Plot')),
                ('release_date', models.DateField(blank=True, help_text='Please use the following format: <em>YYYYMM-DD</em>.', null=True, verbose_name='Release date')),
                ('runtime', models.IntegerField(blank=True, help_text='Please enter an integer value (minutes)', null=True, verbose_name='Runtime')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='film/posters/%Y/%m/%d/', verbose_name='Poster')),
                ('rate', models.FloatField(default=5.0, help_text='Please enter an float value (range 1.0 - 10.0)', null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Rate')),
                ('genres', models.ManyToManyField(help_text='Select a genre for this film', to='movies.genre')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmy',
                'ordering': ['-release_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(null=True, upload_to=movies.models.attachment_path, verbose_name='File')),
                ('type', models.CharField(blank=True, choices=[('audio', 'Audio'), ('image', 'Image'), ('text', 'Text'), ('video', 'Video'), ('other', 'Other')], default='image', help_text='Select allowed attachment type', max_length=10, verbose_name='Attachment type')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.film')),
            ],
            options={
                'verbose_name': 'Příloha',
                'verbose_name_plural': 'Přílohy',
                'ordering': ['-last_update', 'type'],
            },
        ),
    ]