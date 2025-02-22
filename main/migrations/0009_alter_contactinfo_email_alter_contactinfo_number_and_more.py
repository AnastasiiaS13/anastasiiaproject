# Generated by Django 5.1.6 on 2025-02-20 10:48

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_contactinfo_alter_about_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='opening_hours',
            field=ckeditor.fields.RichTextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
