from __future__ import unicode_literals
from itertools import chain

from django.db import migrations


def populate_permissions_lists(apps):
    permission_class = apps.get_model('auth', 'Permission')

    dine_permissions = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                       content_type__model='dine')

    item_permissions = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                       content_type__model='item')

    location_permissions = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                           content_type__model='location')

    rating_permissions = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                         content_type__model='rating')

    recipe_permissions = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                         content_type__model='recipe')

    restaurant_permissions = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                             content_type__model='restaurant')

    reviewer_permissions = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                           content_type__model='reviewer')

    perm_view_dine = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                     content_type__model='dine',
                                                     codename='view_dine')

    perm_view_item = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                     content_type__model='item',
                                                     codename='view_item')

    perm_view_location = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                         content_type__model='location',
                                                         codename='view_location')

    perm_view_rating = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                       content_type__model='rating',
                                                       codename='view_rating')

    perm_view_recipe = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                       content_type__model='recipe',
                                                       codename='view_recipe')

    perm_view_restaurant = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                           content_type__model='restaurant',
                                                           codename='view_restaurant')

    perm_view_reviewer = permission_class.objects.filter(content_type__app_label='restaurantreview',
                                                         content_type__model='reviewer',
                                                         codename='view_reviewer')

    rr_reviewer_permissions = chain(dine_permissions,
                                    reviewer_permissions,
                                    perm_view_restaurant,
                                    perm_view_location,
                                    item_permissions,
                                    rating_permissions,
                                    perm_view_recipe)

    rr_owner_permissions = chain(perm_view_dine,
                                 perm_view_reviewer,
                                 restaurant_permissions,
                                 location_permissions,
                                 perm_view_rating,
                                 perm_view_item,
                                 recipe_permissions
                                 )

    my_groups_initialization_list = [
        {
            "name": "rr_reviewer",
            "permissions_list": rr_reviewer_permissions,
        },
        {
            "name": "rr_owner",
            "permissions_list": rr_owner_permissions,
        }
    ]
    return my_groups_initialization_list


def add_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            group_object.permissions.set(group['permissions_list'])
            group_object.save()


def remove_group_permissions_data(apps, schema_editor):
    groups_initialization_list = populate_permissions_lists(apps)

    group_model_class = apps.get_model('auth', 'Group')
    for group in groups_initialization_list:
        if group['permissions_list'] is not None:
            group_object = group_model_class.objects.get(
                name=group['name']
            )
            list_of_permissions = group['permissions_list']
            for permission in list_of_permissions:
                group_object.permissions.remove(permission)
                group_object.save()


class Migration(migrations.Migration):
    dependencies = [
        ('restaurantreview', '0008_create_groups'),
    ]

    operations = [
        migrations.RunPython(
            add_group_permissions_data,
            remove_group_permissions_data
        )
    ]
