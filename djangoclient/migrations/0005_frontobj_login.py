# Generated by Django 4.2.7 on 2023-12-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoclient', '0004_frontobj_build'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontobj',
            name='login',
            field=models.CharField(default='default', max_length=250),
        ),
    ]
