from datetime import datetime

from django.db import models
from django.db.models import UniqueConstraint


class Reviewer(models.Model):
    reviewer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, unique=True)
    last_name = models.CharField(max_length=45, unique=True)
    email = models.EmailField(max_length=45, unique=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name', 'first_name']
        constraints = [
            UniqueConstraint(fields=['first_name', 'last_name'], name='unique_person')
        ]


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.restaurant_name


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    street_number = models.IntegerField(unique=True)
    street_name = models.CharField(max_length=45, unique=True)
    city = models.CharField(max_length=45, unique=True)
    zipcode = models.IntegerField(unique=True)
    state = models.CharField(max_length=25, unique=True)
    restaurant = models.ForeignKey(Restaurant, related_name="locations", on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s %s, %s %s' % (self.street_number, self.street_name, self.city, self.state, self.zipcode)

    class Meta:
        ordering = ['street_number', 'street_name']
        constraints = [
            UniqueConstraint(fields=['street_number', 'street_name', 'city', 'state'], name='unique_location')
        ]


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=45, unique=True)
    item_cost = models.DecimalField(decimal_places=2, max_digits=6, unique=True)

    def __str__(self):
        return '%s - %s' % (self.item_name, self.item_cost)

    class Meta:
        ordering = ['name', 'cost']


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    stars_rating = models.IntegerField(unique=True)
    comment = models.CharField(max_length=250, unique=True, default='')
    reviewer = models.ForeignKey(Reviewer, related_name="ratings", on_delete=models.PROTECT)
    item = models.ForeignKey(Item, related_name="ratings", on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.stars_rating, self.comment)

    class Meta:
        ordering = ['rating']


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    ingredients = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return '%s' % self.ingredients


class Dine(models.Model):
    dine_at_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey(Location, related_name="dines", on_delete=models.PROTECT)
    reviewer = models.ForeignKey(Reviewer, related_name="dines", on_delete=models.PROTECT)

    def __str__(self):
        return '%s' % self.date

    class Meta:
        ordering = ['date', 'location', 'reviewer']
        constraints = [
            UniqueConstraint(fields=['date', 'location'], name='unique_rating')
        ]
