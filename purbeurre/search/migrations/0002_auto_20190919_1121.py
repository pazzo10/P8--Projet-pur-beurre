# Generated by Django 2.2.5 on 2019-09-19 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categorie',
            new_name='main_categorie',
        ),
    ]
