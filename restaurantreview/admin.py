from django.contrib import admin

from restaurantreview.models import Location, Reviewer, Restaurant, Item, Rating, Recipe, \
    Dine

admin.site.register(Location)
admin.site.register(Reviewer)
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Rating)
admin.site.register(Recipe)
admin.site.register(Dine)
