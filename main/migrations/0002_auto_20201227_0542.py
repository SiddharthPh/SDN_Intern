# Generated by Django 3.1.4 on 2020-12-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='patient_pics'),
        ),
    ]
