# Generated by Django 3.2 on 2021-04-30 19:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='_12th',
            new_name='class12',
        ),
        migrations.AddField(
            model_name='profile',
            name='time_class12',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
