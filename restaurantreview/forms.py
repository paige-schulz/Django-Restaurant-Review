from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import DateField, NumberInput

from restaurantreview.models import Dine, Recipe, Rating, Restaurant, Reviewer, Item, Location


class DineForm(forms.ModelForm):
    class Meta:
        model = Dine
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }

        def clean_location(self):
            return self.cleaned_data['location'].strip()


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

        def clean_item_name(self):
            return self.cleaned_data['item_name'].strip()

        def clean_item_cost(self):
            return self.cleaned_data['item_cost'].strip()


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

        def clean_street_number(self):
            return self.cleaned_data['street_number'].strip()

        def clean_street_name(self):
            return self.cleaned_data['street_name'].strip()

        def clean_city(self):
            return self.cleaned_data['city'].strip()

        def clean_zipcode(self):
            return self.cleaned_data['zipcode'].strip()

        def clean_state(self):
            return self.cleaned_data['state'].strip()


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'

        def clean_stars_rating(self):
            return self.cleaned_data['stars_rating'].strip()

        def clean_comment(self):
            return self.cleaned_data['comment'].strip()


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        def clean_ingredients(self):
            return self.cleaned_data['ingredients'].strip()


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

        def clean_restaurant_name(self):
            return self.cleaned_data['restaurant_name'].strip()


class ReviewerForm(forms.ModelForm):
    class Meta:
        model = Reviewer
        fields = '__all__'

        def clean_first_name(self):
            return self.cleaned_data['first_name'].strip()

        def clean_last_name(self):
            return self.cleaned_data['last_name'].strip()

        def clean_middle_name(self):
            if len(self.cleaned_data['middle_name']) == 0:
                result = self.cleaned_data['middle_name']
            else:
                result = self.cleaned_data['middle_name'].strip()
            return result
