# Generated by Django 4.2.7 on 2023-12-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoclient', '0006_remove_frontobj_axis_remove_frontobj_color_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FrontObj',
        ),
        migrations.AddField(
            model_name='maps',
            name='obj',
            field=models.JSONField(default='default'),
        ),
    ]
