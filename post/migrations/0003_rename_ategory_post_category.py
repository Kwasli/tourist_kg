# Generated by Django 3.2.9 on 2022-03-18 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20220317_2044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ategory',
            new_name='category',
        ),
    ]
