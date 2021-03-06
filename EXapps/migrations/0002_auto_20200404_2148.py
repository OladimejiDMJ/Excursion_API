# Generated by Django 2.2.6 on 2020-04-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EXapps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apidata',
            name='activityLevel',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='collectionType',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='currency',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='externalContent',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='featured',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='language',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='mealInfo',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='portID',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='shortDescription',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='status',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='type',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='typology',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='apidata',
            name='wheelChairAccessible',
            field=models.BooleanField(),
        ),
    ]
