# Generated by Django 3.2.4 on 2021-08-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0004_department_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
