# pylint: skip-file
# Generated by Django 2.2.16 on 2021-03-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dialog_engine', '0007_remove_dialogstatetransition_refresh'),
    ]

    operations = [
        migrations.AddField(
            model_name='dialogscript',
            name='identifier',
            field=models.SlugField(blank=True, max_length=1024, null=True),
        ),
    ]