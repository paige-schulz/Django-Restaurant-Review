from django.urls import path

from restaurantreview.views import (
    ReviewerList, RestaurantList, DineList, ItemList, LocationList, RatingList, RecipeList, RestaurantDetail,
    DineDetail, ItemDetail, LocationDetail, RatingDetail, ReviewerDetail
)

urlpatterns = [
    path('reviewer/',
         ReviewerList.as_view(),
         name='restaurantreview_reviewer_list_urlpattern'),
    path('reviewer/<int:pk>/',
         ReviewerDetail.as_view(),
         name='restaurantreview_reviewer_detail_urlpattern'),
    path('restaurant/',
         RestaurantList.as_view(),
         name='restaurantreview_restaurant_list_urlpattern'),
    path('restaurant/<int:pk>/',
         RestaurantDetail.as_view(),
         name='restaurantreview_restaurant_detail_urlpattern'),
    path('dine/',
         DineList.as_view(),
         name='restaurantreview_dine_list_urlpattern'),
    path('dine/<int:pk>/',
         DineDetail.as_view(),
         name='restaurantreview_dine_detail_urlpattern'),
    path('item/',
         ItemList.as_view(),
         name='restaurantreview_item_list_urlpattern'),
    path('item/<int:pk>/',
         ItemDetail.as_view(),
         name='restaurantreview_item_detail_urlpattern'),
    path('location/',
         LocationList.as_view(),
         name='restaurantreview_location_list_urlpattern'),
    path('location/<int:pk>/',
         LocationDetail.as_view(),
         name='restaurantreview_location_detail_urlpattern'),
    path('recipe/',
         RecipeList.as_view(),
         name='restaurantreview_recipe_list_urlpattern'),
    path('rating/',
         RatingList.as_view(),
         name='restaurantreview_rating_list_urlpattern'),
    path('rating/<int:pk>/',
         RatingDetail.as_view(),
         name='restaurantreview_rating_detail_urlpattern'),

]
