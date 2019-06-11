# Generated by Django 2.1.3 on 2019-05-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0007_auto_20190516_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='calipsocontainer',
            name='hdd_allocated',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='calipsocontainer',
            name='memory_allocated',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='calipsocontainer',
            name='num_cpus',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='historicalcalipsocontainer',
            name='hdd_allocated',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='historicalcalipsocontainer',
            name='memory_allocated',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='historicalcalipsocontainer',
            name='num_cpus',
            field=models.IntegerField(null=True),
        ),
    ]
