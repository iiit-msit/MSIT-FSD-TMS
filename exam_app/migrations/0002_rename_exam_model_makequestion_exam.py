# Generated by Django 4.0.3 on 2022-04-28 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='makequestion',
            old_name='exam_model',
            new_name='exam',
        ),
    ]
