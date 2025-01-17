# Generated by Django 5.0.1 on 2024-07-19 12:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userform'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('lname', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('webname', models.CharField(max_length=100, null=True)),
                ('massage', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='contactEnquary',
        ),
    ]
