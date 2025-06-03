from django.shortcuts import render, redirect
from . import utils

def home(request):
    # heroes = utils.get_all_heroes()
    # rankings = utils.get_hero_rankings()
    # return render(request, 'home.html', {'heroes': heroes, 'rankings': rankings, })
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')