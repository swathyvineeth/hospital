# Generated by Django 3.2.4 on 2021-08-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0003_auto_20210802_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='img',
            field=models.ImageField(default=1, upload_to='depart'),
            preserve_default=False,
        ),
    ]
