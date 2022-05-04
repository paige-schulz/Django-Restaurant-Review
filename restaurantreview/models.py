from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Reviewer(models.Model):
    reviewer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, unique=True)
    middle_name = models.CharField(max_length=45, blank=True, default='')

    def __str__(self):
        result = ''
        if self.middle_name == '':
            result = '%s %s' % (self.first_name, self.last_name)
        else:
            result = '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        return result

    def get_absolute_url(self):
        return reverse('restaurantreview_reviewer_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('restaurantreview_reviewer_delete_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('restaurantreview_reviewer_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'middle_name']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'middle_name'], name='unique_reviewer')
        ]


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.restaurant_name

    def get_absolute_url(self):
        return reverse('restaurantreview_restaurant_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('restaurantreview_restaurant_delete_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('restaurantreview_restaurant_update_urlpattern',
                       kwargs={'pk': self.pk})


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    ingredients = models.CharField(max_length=55, default='')

    def __str__(self):
        return '%s' % self.ingredients

    def get_absolute_url(self):
        return reverse('restaurantreview_recipe_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('restaurantreview_recipe_delete_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('restaurantreview_recipe_update_urlpattern',
                       kwargs={'pk': self.pk})


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_number = models.IntegerField(unique=True)
    street_name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    zipcode = models.IntegerField(max_length=10)
    state = models.CharField(max_length=25)
    restaurant = models.ForeignKey(Restaurant, related_name="locations", on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s %s, %s %s' % (self.street_number, self.street_name, self.city, self.state, self.zipcode)

    def get_absolute_url(self):
        return reverse('restaurantreview_location_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('restaurantreview_location_delete_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('restaurantreview_location_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['street_number', 'street_name']
        constraints = [
            UniqueConstraint(fields=['street_number', 'street_name', 'city', 'state'], name='unique_location')
        ]


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=45)
    item_cost = models.DecimalField(decimal_places=2, max_digits=6)
    recipe = models.ForeignKey(Recipe, related_name="items", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '%s - %s' % (self.item_name, self.item_cost)

    def get_absolute_url(self):
        return reverse('restaurantreview_item_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('restaurantreview_item_delete_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('restaurantreview_item_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['item_name', 'item_cost']


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    stars_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comment = models.CharField(max_length=250, default='')
    reviewer = models.ForeignKey(Reviewer, related_name="ratings", on_delete=models.PROTECT)
    item = models.ForeignKey(Item, related_name="ratings", on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.stars_rating, self.comment)

    def get_absolute_url(self):
        return reverse('restaurantreview_rating_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('restaurantreview_rating_delete_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('restaurantreview_rating_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['stars_rating']


class Dine(models.Model):
    dine_at_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location, related_name="dines", on_delete=models.PROTECT)
    reviewer = models.ForeignKey(Reviewer, related_name="dines", on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.date

    def get_absolute_url(self):
        return reverse('restaurantreview_dine_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('restaurantreview_dine_delete_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('restaurantreview_dine_update_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['date', 'location', 'reviewer']
        constraints = [
            UniqueConstraint(fields=['date', 'location'], name='unique_rating')
        ]
