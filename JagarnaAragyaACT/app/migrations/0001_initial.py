# Generated by Django 4.2.2 on 2023-06-27 09:57

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(upload_to='aboutimage/')),
                ('discriptions', ckeditor.fields.RichTextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='file/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='blogimages/')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('discriptions', ckeditor.fields.RichTextField()),
                ('act_slug', autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='blog_title', unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CustomerQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(upload_to='galleryimage/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='noticeimages/')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('discriptions', ckeditor.fields.RichTextField()),
                ('notic_slug', autoslug.fields.AutoSlugField(default=None, editable=False, populate_from='title', unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sliderimage/')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMemeber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='teamimage/')),
                ('position', models.CharField(max_length=150)),
                ('discriptions', ckeditor.fields.RichTextField(blank=True, max_length=250, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
