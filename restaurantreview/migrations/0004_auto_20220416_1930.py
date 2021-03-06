# Generated by Django 3.2.5 on 2022-04-16 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantreview', '0003_auto_20220415_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='items', to='restaurantreview.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default='', max_length=55),
        ),
    ]
