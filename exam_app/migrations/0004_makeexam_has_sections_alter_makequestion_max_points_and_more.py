# Generated by Django 4.0.3 on 2022-04-26 07:10

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam_app', '0003_userquestiondetails_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='makeexam',
            name='has_sections',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='makequestion',
            name='max_points',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='makequestion',
            name='question_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='userexamdetails',
            name='status',
            field=models.CharField(default='Yet To Take', max_length=64),
        ),
        migrations.AlterField(
            model_name='userquestiondetails',
            name='points',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.CreateModel(
            name='MakeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=124)),
                ('sub_title', models.CharField(blank=True, max_length=124)),
                ('instructions', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='')),
                ('exam', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='exam_app.makeexam')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='makequestion',
            name='section',
            field=models.ManyToManyField(blank=True, default='', to='exam_app.makesection'),
        ),
    ]
