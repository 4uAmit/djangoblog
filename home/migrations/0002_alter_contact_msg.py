# Generated by Django 3.2.7 on 2021-11-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.CharField(max_length=1000),
        ),
    ]
