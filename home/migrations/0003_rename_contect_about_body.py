# Generated by Django 4.2.1 on 2023-05-29 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contect1_about_contect_remove_about_contect2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='contect',
            new_name='body',
        ),
    ]
