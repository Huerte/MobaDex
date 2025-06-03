from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('matchups/', views.hero_matchups, name='matchups'),
    path('about/', views.about, name='about'),
    # API endpoints
    # path('api/heroes/', views.api_hero_list, name='api_hero_list'),
    # path('api/heroes/<int:hero_id>/counters/', views.api_hero_counters, name='api_hero_counters'),
    # path('api/heroes/<int:hero_id>/synergies/', views.api_hero_synergies, name='api_hero_synergies'),
    # path('api/heroes/<int:hero_id>/stats/', views.api_hero_stats, name='api_hero_stats'),
]
