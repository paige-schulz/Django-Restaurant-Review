from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('restaurantreview_item_list_urlpattern')
