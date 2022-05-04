from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import DateField, NumberInput

from restaurantreview.models import Dine, Recipe, Rating, Restaurant, Reviewer, Item, Location


# class InstructorForm(forms.ModelForm):
#     class Meta:
#         model = Instructor
#         fields = '__all__'
#
#         def clean_first_name(self):
#             return self.cleaned_data['first_name'].strip()
#
#         def clean_last_name(self):
#             return self.cleaned_data['last_name'].strip()
#
#         def clean_disambiguator(self):
#             if len(self.cleaned_data['disambiguator']) == 0:
#                 result = self.cleaned_data['disambiguator']
#             else:
#                 result = self.cleaned_data['disambiguator'].strip()
#             return result
#
#
# class SectionForm(forms.ModelForm):
#     class Meta:
#         model = Section
#         fields = '__all__'
#
#         def clean_section_name(self):
#             return self.cleaned_data['section_name'].strip()
#
#
# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = '__all__'
#
#         def clean_course_number(self):
#             return self.cleaned_data['course_number'].strip()
#
#         def clean_course_name(self):
#             return self.cleaned_data['course_name'].strip()
#
#
# class SemesterForm(forms.ModelForm):
#     class Meta:
#         model = Semester
#         fields = '__all__'
#
#
# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'
#
#         def clean_first_name(self):
#             return self.cleaned_data['first_name'].strip()
#
#         def clean_last_name(self):
#             return self.cleaned_data['last_name'].strip()
#
#         def clean_disambiguator(self):
#             if len(self.cleaned_data['disambiguator']) == 0:
#                 result = self.cleaned_data['disambiguator']
#             else:
#                 result = self.cleaned_data['disambiguator'].strip()
#             return result


class DineForm(forms.ModelForm):
    class Meta:
        model = Dine
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'


class ReviewerForm(forms.ModelForm):
    class Meta:
        model = Reviewer
        fields = '__all__'
