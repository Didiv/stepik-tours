from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseNotFound
from tours.data import *


class MainView(View):
    def get(self, request):
        return render(
            request, 'tours/index.html', context={
                "title": title,
                "subtitle": subtitle,
                "description": description,
                "departures": departures,
                "tours": tours,
            }
        )


class DepartureView(View):
    def get(self, request, departure: str):
        if departure not in departures:
            return HttpResponseNotFound(
                f'Вылет из {departure} не поддерживается')
        tours_filtered = dict(
            filter(
                lambda x: x[1]['departure'] == departure,
                tours.items()))
        min_price = min(
            tours_filtered.values(),
            key=lambda x: x['price'])['price']
        max_price = max(
            tours_filtered.values(),
            key=lambda x: x['price'])['price']
        min_nights = min(
            tours_filtered.values(),
            key=lambda x: x['nights'])['nights']
        max_nights = max(
            tours_filtered.values(),
            key=lambda x: x['nights'])['nights']
        return render(
            request, 'tours/departure.html', context={
                "title": title,
                "subtitle": subtitle,
                "description": description,
                "departures": departures,
                "departure": departure,
                "departure_name": departures[departure],
                "tours": tours_filtered,
                "min_price": min_price,
                "max_price": max_price,
                "min_nights": min_nights,
                "max_nights": max_nights,
            }
        )


class TourView(View):
    def get(self, request, id: int):
        if id not in tours:
            return HttpResponseNotFound(
                f'Тур с id {id} нам не известен')
        return render(
            request, 'tours/tour.html', context={
                "title": title,
                "departures": departures,
                "tour": tours[id],
                "departure_name": departures[tours[id]['departure']]
            }
        )
