# Generated by Django 3.2.5 on 2022-05-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantreview', '0009_create_group_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='', max_length=155),
        ),
    ]
