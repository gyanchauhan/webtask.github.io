# Generated by Django 4.1.3 on 2024-07-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_contact_form_delete_app_delete_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_form',
            name='Message',
            field=models.CharField(max_length=10000000000000, null=True),
        ),
    ]
