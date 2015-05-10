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
    def get(selfself, request, *args, **kwargs):
        from shows.models import show
        # futureshows=shows.objects.filter(showDate__gte=datetime.datetime.now())
        futureshows=show.objects.filter(showDate__gte='2005-01-01')
        orderedfutureshows=sorted(futureshows, key=lambda i:i.showDate)
        p = Paginator(orderedfutureshows, 20)
        # requestpage = request.GET.get('page')
        requestpage=1
        try:
            shows=p.page(requestpage)
        except PageNotAnInteger:
            shows=p.page(1)
        except EmptyPage:
            shows=p.page(p.num_pages)

        showslist = serializers.serialize("json", shows)

        return showslist

