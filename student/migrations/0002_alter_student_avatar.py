# Generated by Django 5.0.3 on 2024-03-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='student_pics'),
        ),
    ]
