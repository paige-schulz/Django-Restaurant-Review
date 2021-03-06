# Generated by Django 3.2.5 on 2022-04-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantreview', '0002_auto_20220403_2127'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='reviewer',
            name='unique_person',
        ),
        migrations.AlterField(
            model_name='item',
            name='item_cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='location',
            name='street_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='first_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='reviewer',
            name='last_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AddConstraint(
            model_name='reviewer',
            constraint=models.UniqueConstraint(fields=('last_name', 'first_name', 'middle_name'), name='unique_reviewer'),
        ),
    ]
