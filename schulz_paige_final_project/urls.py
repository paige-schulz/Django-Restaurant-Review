from django.contrib import admin
from django.urls import path, include

# from restaurantreview.views import (
#     reviewer_list_view, dine_list_view, item_list_view, location_list_view, rating_list_view, recipe_list_view,
#     restaurant_list_view
# )
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(
        pattern_name='restaurantreview_restaurant_list_urlpattern',
        permanent=False
    )),
    path('', include('restaurantreview.urls'))

]
