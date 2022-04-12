# Generated by Django 4.0.3 on 2022-04-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0008_alter_makequestion_difficulty_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makequestion',
            name='difficulty_level',
            field=models.CharField(default='None', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='makequestion',
            name='max_points',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='makequestion',
            name='max_time',
            field=models.DurationField(null=True),
        ),
    ]
