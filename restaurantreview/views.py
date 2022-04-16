from django.shortcuts import render

from restaurantreview.models import Reviewer, Dine, Item, Location, Recipe, Rating, Restaurant
from django.views.generic import ListView, DetailView


class ReviewerList(ListView):
    model = Reviewer


class ReviewerDetail(DetailView):
    model = Reviewer

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        reviewer = self.get_object()
        dine_list = reviewer.dines.all()
        rating_list = reviewer.ratings.all()
        context['dine_list'] = dine_list
        context['rating_list'] = rating_list
        return context


class RestaurantList(ListView):
    model = Restaurant


class RestaurantDetail(DetailView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        restaurant = self.get_object()
        location_list = restaurant.locations.all()
        context['location_list'] = location_list
        return context


class DineList(ListView):
    model = Dine


class DineDetail(DetailView):
    model = Dine

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dine = self.get_object()
        location = dine.location
        reviewer = dine.reviewer
        context['location'] = location
        context['reviewer'] = reviewer
        return context


class ItemList(ListView):
    model = Item


class ItemDetail(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        item = self.get_object()
        rating_list = item.ratings.all()
        context['rating_list'] = rating_list
        return context


class LocationList(ListView):
    model = Location


class LocationDetail(DetailView):
    model = Location

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        location = self.get_object()
        restaurant = location.restaurant
        context['restaurant'] = restaurant
        return context


class RatingList(ListView):
    model = Rating


class RatingDetail(DetailView):
    model = Rating

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        rating = self.get_object()
        reviewer = rating.reviewer
        item = rating.item
        context['reviewer'] = reviewer
        context['item'] = item
        return context


class RecipeList(ListView):
    model = Recipe
