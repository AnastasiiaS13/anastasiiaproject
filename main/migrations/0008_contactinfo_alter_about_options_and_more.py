# Generated by Django 5.1.6 on 2025-02-20 10:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=100)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=500)),
                ('opening_hours', ckeditor.fields.RichTextField()),
                ('facebook_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('linkedin_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('pinterest_link', models.URLField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ('sort', 'name'), 'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('sort', 'name'), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ('sort', 'name'), 'verbose_name_plural': 'Slides'},
        ),
    ]
