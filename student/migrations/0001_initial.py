# Generated by Django 5.0.3 on 2024-03-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=10)),
                ('avatar', models.ImageField(upload_to='student_pics')),
            ],
        ),
    ]
