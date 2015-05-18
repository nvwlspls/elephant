from django.shortcuts import render

# Create your views here.


# Create your views here.
import datetime
import csv
import json

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator
from django.core import serializers

from django.views.generic import TemplateView, View, ListView, \
    UpdateView, DeleteView, CreateView, FormView


class angularHome(View):
    def get(self, request, *args, **kwargs):

        return render_to_response('base.html',
                                  context_instance=RequestContext(request))

class getshows(View):
    """
    class to retrieve shows and return them in a json format
    """
    def get(self, request, pagenum, *args, **kwargs):
        from shows.models import show
        # futureshows=shows.objects.filter(showDate__gte=datetime.datetime.now())
        futureshows=show.objects.filter(showDate__gte='2005-01-01')
        orderedfutureshows=sorted(futureshows, key=lambda i:i.showDate)

        futureshowsdict = {}

        for i in orderedfutureshows:
            futureshows[i.showID] = i.as_json()


        p = Paginator(orderedfutureshows, 20)
        requestpage=pagenum
        try:
            shows=p.page(requestpage)
        except PageNotAnInteger:
            shows=p.page(1)
        except EmptyPage:
            shows=p.page(p.num_pages)

        showslist = serializers.serialize("json", shows, use_natural_foreign_keys=True)

        return HttpResponse(showslist)
        # return HttpResponse("<h1>a[[</h1>")

class matchbands(View):
    """
    match bands from the text search field
    """
    def get(self, request, bandtext ,*args, **kwargs):
        from shows.models import band
        bandlist=band.objects.filter(bandName__icontains=bandtext)

        jsonbandslist=serializers.serialize("json", bandlist, use_natural_foreign_keys=True)

        return HttpResponse(jsonbandslist)

class getfutureshows(View):
    """
    A class to retrieve all shows who's time is in the FUTURE!!!!
    """
    def get(selfself, request, *args, **kwargs):
        from shows.models import show
        # # futureshows=shows.objects.filter(showDate__gte=datetime.datetime.now())
        futureshows=show.objects.filter(showDate__gte='2005-01-01')
        orderedfutureshows =sorted(futureshows, key=lambda i:i.showDate)

        return HttpResponse(serializers.serialize("json", orderedfutureshows, use_natural_foreign_keys=True))