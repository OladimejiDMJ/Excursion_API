# Generated by Django 2.2.6 on 2020-04-22 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EXapps', '0007_auto_20200409_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apidata',
            old_name='pricelevel',
            new_name='priceLevel',
        ),
    ]