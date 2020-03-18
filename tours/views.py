from django.shortcuts import render
from django.views.generic import View

from data import *


class MainView(View):
    def get(self, request):
        return render


class DepartureView(View):
    def get(self, request, deparure: str):
        return HttpResponse('Ans')


class TourView(View):
    def get(self, request, id: int):
        return HttpResponse(title)

