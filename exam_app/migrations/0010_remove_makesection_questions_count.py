# Generated by Django 4.0.3 on 2022-04-22 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0009_alter_makequestion_question_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='makesection',
            name='questions_count',
        ),
    ]