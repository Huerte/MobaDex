from django.shortcuts import render, redirect
from math import ceil
from . import utils

def home(request):
    heroes = utils.all_heroes()
    context = {
        'heroes': heroes,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def matchup_page(request):
    days_options = [1, 3, 7, 15, 30]
    rank_options = ["all", "epic", "legend", "mythic", "honor", "glory"]
    sort_fields = ["pick_rate", "ban_rate", "win_rate"]
    sort_orders = ["asc", "desc"]

    days = request.GET.get('days', '1')
    rank = request.GET.get('rank', 'all')
    size = int(request.GET.get('size', 127))
    index = int(request.GET.get('index', 1))
    sort_field = request.GET.get('sort_field', 'win_rate')
    sort_order = request.GET.get('sort_order', 'desc')

    records, total_count = utils.hero_rank(days, rank, size, index, sort_field, sort_order)

    total_pages = ceil(total_count / size)

    context = {
        "days_options": days_options,
        "rank_options": rank_options,
        "sort_fields": sort_fields,
        "sort_orders": sort_orders,
        "records": records,
        "current_page": index,
        "total_pages": total_pages,
        "page_range": range(max(index - 2, 1), min(index + 3, total_pages + 1)),
        "page_offset": (index - 1) * size,
        "selected_days": days,
        "selected_rank": rank,
        "selected_sort_field": sort_field,
        "selected_sort_order": sort_order,
    }

    return render(request, "matchup.html", context)