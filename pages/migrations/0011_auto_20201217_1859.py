# Generated by Django 3.0.8 on 2020-12-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20201217_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(default='', help_text='Add a title for this specific event.', max_length=100),
        ),
    ]
