# Generated by Django 2.2.8 on 2020-01-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0011_auto_20191209_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='text',
            field=models.TextField(),
        ),
    ]
