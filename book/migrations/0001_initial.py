# Generated by Django 4.1.3 on 2022-11-16 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=6, validators=[django.core.validators.MinLengthValidator(5, 'code cannot be less than a length 5'), django.core.validators.MaxLengthValidator(5, 'code can only be length of 5')])),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('isbn', models.CharField(max_length=20)),
                ('date_published', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('edition', models.PositiveSmallIntegerField()),
                ('genre', models.CharField(choices=[('C', 'Comedy'), ('T', 'Tragedy'), ('TC', 'Tragicomedy'), ('CR', 'Crime'), ('R', 'Romance'), ('SF', 'Science Fiction')], default='R', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
    ]
