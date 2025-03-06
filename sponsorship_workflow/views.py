from django.db.models import Avg, Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page

from sponsorship_workflow.models import Sponsor

# Create your views here.

# def index(request):
#     print('Request for index page received')
#     restaurants = Restaurant.objects.annotate(avg_rating=Avg('review__rating')).annotate(review_count=Count('review'))
#     lastViewedRestaurant = request.session.get("lastViewedRestaurant", False)
#     return render(request, 'sponsorship_workflow/index.html', {'LastViewedRestaurant': lastViewedRestaurant, 'restaurants': restaurants})
def index(request):
    print('Request for index page received')
    return render(request, 'sponsorship_workflow/index.html')

def sponsors(request):
    print('Request for sponsors page received')

    return render(request, 'sponsorship_workflow/sponsors.html')

@cache_page(60)
def details(request, id):
    print('Request for sponsor details page received')
    sponsor = get_object_or_404(Sponsor, pk=id)
    return render(request, 'sponsorship_workflow/details.html', {'sponsor': sponsor})


def create_sponsor(request):
    print('Request for add sponsor page received')
    return render(request, 'sponsorship_workflow/add_sponsor.html')


@csrf_exempt
def add_sponsor(request):
    # try:
    #     name = request.POST['restaurant_name']
    #     street_address = request.POST['street_address']
    #     description = request.POST['description']
    # except (KeyError):
    #     # Redisplay the form
    #     return render(request, 'sponsorship_workflow/add_restaurant.html', {
    #         'error_message': "You must include a restaurant name, address, and description",
    #     })
    # else:
    #     restaurant = Restaurant()
    #     restaurant.name = name
    #     restaurant.street_address = street_address
    #     restaurant.description = description
    #     Restaurant.save(restaurant)
    #     Restaurant.save(restaurant)
    try:
        name = request.POST['restaurant_name']
        street_address = request.POST['street_address']
        description = request.POST['description']
    except (KeyError):
        # Redisplay the form
        return render(request, 'sponsorship_workflow/add_restaurant.html', {
            'error_message': "You must include a restaurant name, address, and description",
        })
    else:
        restaurant = Restaurant()
        restaurant.name = name
        restaurant.street_address = street_address
        restaurant.description = description
        Restaurant.save(restaurant)
        Sponsor.save(restaurant)

        return HttpResponseRedirect(reverse('details', args=(sponsor.id,)))
