# Generated by Django 4.2.14 on 2024-08-19 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_resume', '0005_education'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='desciption',
            new_name='description',
        ),
    ]
