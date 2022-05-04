from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from restaurantreview.forms import DineForm, ItemForm, ReviewerForm, RestaurantForm, LocationForm, RatingForm, \
    RecipeForm
from restaurantreview.models import Reviewer, Dine, Item, Location, Recipe, Rating, Restaurant
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .utils import PageLinksMixin


class ReviewerList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Reviewer
    permission_required = 'restaurantreview.view_reviewer'


class ReviewerDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Reviewer
    permission_required = 'restaurantreview.view_reviewer'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        reviewer = self.get_object()
        dine_list = reviewer.dines.all()
        rating_list = reviewer.ratings.all()
        context['dine_list'] = dine_list
        context['rating_list'] = rating_list
        return context


class ReviewerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ReviewerForm
    model = Reviewer
    permission_required = 'restaurantreview.add_reviewer'


class ReviewerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Reviewer
    success_url = reverse_lazy('restaurantreview_reviewer_list_urlpattern')
    permission_required = 'restaurantreview.delete_reviewer'

    def get(self, request, pk):
        reviewer = get_object_or_404(Reviewer, pk=pk)
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
        if ratings.count() > 0:
            return render(
                request,
                'restaurantreview/reviewer_refuse_delete.html',
                {'reviewer': reviewer,
                 'ratings': ratings,
                 }
            )
        else:
            return render(
                request,
                'restaurantreview/reviewer_confirm_delete.html',
                {'reviewer': reviewer}
            )


class ReviewerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ReviewerForm
    model = Reviewer
    template_name = 'restaurantreview/reviewer_form_update.html'
    permission_required = 'restaurantreview.change_reviewer'


class RestaurantList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Restaurant
    permission_required = 'restaurantreview.view_restaurant'


class RestaurantDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Restaurant
    permission_required = 'restaurantreview.view_restaurant'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        restaurant = self.get_object()
        location_list = restaurant.locations.all()
        context['location_list'] = location_list
        return context


class RestaurantCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RestaurantForm
    model = Restaurant
    permission_required = 'restaurantreview.add_restaurant'


class RestaurantDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurantreview_restaurant_list_urlpattern')
    permission_required = 'restaurantreview.delete_restaurant'

    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        # registrations = section.registrations.all()
        # dines = restaurant.dines.all()
        locations = restaurant.locations.all()
        if locations.count() > 0:
            return render(
                request,
                'restaurantreview/restaurant_refuse_delete.html',
                {'restaurant': restaurant,
                 'locations': locations,
                 }
            )
        else:
            return render(
                request,
                'restaurantreview/restaurant_confirm_delete.html',
                {'restaurant': restaurant}
            )


class RestaurantUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RestaurantForm
    model = Restaurant
    template_name = 'restaurantreview/restaurant_form_update.html'
    permission_required = 'restaurantreview.change_restaurant'


class DineList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Dine
    permission_required = 'restaurantreview.view_dine'


class DineDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Dine
    permission_required = 'restaurantreview.view_dine'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        dine = self.get_object()
        location = dine.location
        reviewer = dine.reviewer
        context['location'] = location
        context['reviewer'] = reviewer
        return context


class DineCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = DineForm
    model = Dine
    permission_required = 'restaurantreview.add_dine'


class DineDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Dine
    success_url = reverse_lazy('restaurantreview_dine_list_urlpattern')
    permission_required = 'restaurantreview.delete_dine'


class DineUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = DineForm
    model = Dine
    template_name = 'restaurantreview/dine_form_update.html'
    permission_required = 'restaurantreview.change_dine'


class ItemList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Item
    permission_required = 'restaurantreview.view_item'


class ItemDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('restaurantreview_item_list_urlpattern')
    permission_required = 'restaurantreview.delete_item'

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        ratings = item.ratings.all()
        if ratings.count() > 0:
            return render(
                request,
                'restaurantreview/item_refuse_delete.html',
                {'item': item,
                 'ratings': ratings,
                 }
            )
        else:
            return render(
                request,
                'restaurantreview/item_confirm_delete.html',
                {'item': item}
            )


class ItemDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Item
    permission_required = 'restaurantreview.view_item'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        item = self.get_object()
        rating_list = item.ratings.all()
        recipe = item.recipe
        context['rating_list'] = rating_list
        context['recipe'] = recipe
        return context


class ItemCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = ItemForm
    model = Item
    permission_required = 'restaurantreview.add_item'


class ItemUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = ItemForm
    model = Item
    template_name = 'restaurantreview/item_form_update.html'
    permission_required = 'restaurantreview.change_item'


class LocationList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Location
    permission_required = 'restaurantreview.view_location'


class LocationDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Location
    permission_required = 'restaurantreview.view_location'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        location = self.get_object()
        restaurant = location.restaurant
        context['restaurant'] = restaurant
        return context


class LocationCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = LocationForm
    model = Location
    permission_required = 'restaurantreview.add_location'


class LocationDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('restaurantreview_location_list_urlpattern')
    permission_required = 'restaurantreview.delete_location'

    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        dines = location.dines.all()
        if dines.count() > 0:
            return render(
                request,
                'restaurantreview/location_refuse_delete.html',
                {'location': location,
                 'dines': dines,
                 }
            )
        else:
            return render(
                request,
                'restaurantreview/location_confirm_delete.html',
                {'location': location}
            )


class LocationUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = LocationForm
    model = Location
    template_name = 'restaurantreview/location_form_update.html'
    permission_required = 'restaurantreview.change_location'


class RatingList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Rating
    permission_required = 'restaurantreview.view_rating'


class RatingDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Rating
    permission_required = 'restaurantreview.view_rating'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        rating = self.get_object()
        reviewer = rating.reviewer
        item = rating.item
        context['reviewer'] = reviewer
        context['item'] = item
        return context


class RatingCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RatingForm
    model = Rating
    permission_required = 'restaurantreview.add_rating'


class RatingDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Rating
    success_url = reverse_lazy('restaurantreview_rating_list_urlpattern')
    permission_required = 'restaurantreview.delete_rating'


class RatingUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RatingForm
    model = Rating
    template_name = 'restaurantreview/rating_form_update.html'
    permission_required = 'restaurantreview.change_rating'


class RecipeList(LoginRequiredMixin, PermissionRequiredMixin, PageLinksMixin, ListView):
    model = Recipe
    permission_required = 'restaurantreview.view_recipe'


class RecipeDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Recipe
    permission_required = 'restaurantreview.view_recipe'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        recipe = self.get_object()
        item_list = recipe.items.all()
        context['item_list'] = item_list
        return context


class RecipeCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = RecipeForm
    model = Recipe
    permission_required = 'restaurantreview.add_recipe'


class RecipeDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('restaurantreview_recipe_list_urlpattern')
    permission_required = 'restaurantreview.delete_recipe'

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        items = recipe.items.all()
        if items.count() > 0:
            return render(
                request,
                'restaurantreview/recipe_refuse_delete.html',
                {'recipe': recipe,
                 'items': items,
                 }
            )
        else:
            return render(
                request,
                'restaurantreview/recipe_confirm_delete.html',
                {'recipe': recipe}
            )


class RecipeUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'restaurantreview/recipe_form_update.html'
    permission_required = 'restaurantreview.change_recipe'
