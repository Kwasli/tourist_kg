# Generated by Django 3.2.9 on 2022-03-18 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_ategory_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активный'),
        ),
    ]
