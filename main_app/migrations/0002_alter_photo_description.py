# Generated by Django 4.0.4 on 2022-05-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
