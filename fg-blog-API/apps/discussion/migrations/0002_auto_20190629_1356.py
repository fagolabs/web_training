# Generated by Django 2.2.2 on 2019-06-29 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='comment_parent',
            new_name='parent',
        ),
    ]