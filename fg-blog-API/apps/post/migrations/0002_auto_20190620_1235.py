# Generated by Django 2.2.2 on 2019-06-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('draft_public', 'draft_public'), ('public', 'public')], default='draft', max_length=64),
        ),
    ]
