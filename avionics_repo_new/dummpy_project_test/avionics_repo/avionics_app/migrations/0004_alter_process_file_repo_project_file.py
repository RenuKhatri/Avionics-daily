# Generated by Django 3.2.9 on 2022-08-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avionics_app', '0003_alter_process_file_repo_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process_file_repo',
            name='project_file',
            field=models.TextField(),
        ),
    ]
