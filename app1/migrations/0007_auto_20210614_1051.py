# Generated by Django 3.2.3 on 2021-06-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20210612_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner_work',
            name='place',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='worker',
            name='rating',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
