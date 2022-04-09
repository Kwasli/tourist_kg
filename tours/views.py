from django.shortcuts import render
from django.http import Http404


# Create your views here.

from tours.models import Tour, RegularToure

def get_tour_list(request):
    tours = Tour.objects.filter(is_active=True)
    context = {
        "tours":tours
    }
    return render(request, 'tour_list.html', context=context)

def get_tout_detail(request, pk):
    try:
        tour = Tour.objects.get(id = pk)
    except Tour.DoesNotExist:
        raise Http404
    context = {'tour':tour}
    return render(request, 'tour_detail.html', context)