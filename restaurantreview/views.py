from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from restaurantreview.forms import DineForm, ItemForm, ReviewerForm, RestaurantForm, LocationForm, RatingForm, \
    RecipeForm
from restaurantreview.models import Reviewer, Dine, Item, Location, Recipe, Rating, Restaurant
from django.views.generic import ListView, DetailView, CreateView, DeleteView


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


class ReviewerCreate(CreateView):
    form_class = ReviewerForm
    model = Reviewer
    # permission_required = 'restaurantreview.add_dine'


class ReviewerDelete(DeleteView):
    model = Reviewer
    success_url = reverse_lazy('restaurantreview_reviewer_list_urlpattern')

    # permission_required = 'courseinfo.delete_section'

    def get(self, request, pk):
        reviewer = get_object_or_404(Reviewer, pk=pk)
        # registrations = section.registrations.all()
        dines = reviewer.dines.all()
        ratings = reviewer.dines.all()
        if dines.count() > 0:
            return render(
                request,
                'restaurantreview/reviewer_refuse_delete.html',
                {'reviewer': reviewer,
                 'dines': dines,
                 }
            )
        # if ratings.count() > 0:
        #     return render(
        #         request,
        #         'restaurantreview/reviewer_refuse_delete.html',
        #         {'reviewer': reviewer,
        #          'ratings': ratings,
        #          }
        #     )
        else:
            return render(
                request,
                'restaurantreview/reviewer_confirm_delete.html',
                {'reviewer': reviewer}
            )


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


class RestaurantCreate(CreateView):
    form_class = RestaurantForm
    model = Restaurant
    # permission_required = 'restaurantreview.add_dine'


class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurantreview_restaurant_list_urlpattern')

    # permission_required = 'courseinfo.delete_section'

    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        # registrations = section.registrations.all()
        # dines = restaurant.dines.all()
        location = restaurant.locations.all()
        if location.count() > 0:
            return render(
                request,
                'restaurantreview/restaurant_refuse_delete.html',
                {'restaurant': restaurant,
                 'location': location,
                 }
            )
        else:
            return render(
                request,
                'restaurantreview/restaurant_confirm_delete.html',
                {'restaurant': restaurant}
            )


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


class DineCreate(CreateView):
    form_class = DineForm
    model = Dine
    # permission_required = 'restaurantreview.add_dine'


class ItemList(ListView):
    model = Item


class ItemDetail(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        item = self.get_object()
        rating_list = item.ratings.all()
        recipe = item.recipe
        context['rating_list'] = rating_list
        context['recipe'] = recipe
        return context


class ItemCreate(CreateView):
    form_class = ItemForm
    model = Item
    # permission_required = 'restaurantreview.add_item'


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


class LocationCreate(CreateView):
    form_class = LocationForm
    model = Location
    # permission_required = 'restaurantreview.add_dine'


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


class RatingCreate(CreateView):
    form_class = RatingForm
    model = Rating
    # permission_required = 'restaurantreview.add_dine'


class RecipeList(ListView):
    model = Recipe


class RecipeDetail(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        recipe = self.get_object()
        item_list = recipe.items.all()
        context['item_list'] = item_list
        return context


class RecipeCreate(CreateView):
    form_class = RecipeForm
    model = Recipe
    # permission_required = 'restaurantreview.add_dine'
