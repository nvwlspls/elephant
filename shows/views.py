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

from django.views.generic import TemplateView, View, ListView, \
    UpdateView, DeleteView, CreateView, FormView


class angularHome(View):
    def get(self, request, *args, **kwargs):
        import json

        bands = [
            {
                'name': 'metallica',
                'genre': 'Rock',
                'state': 'California',
                'id': '1'
            },
            {
                'name': 'band religion',
                'genre': 'punk',
                'state': 'California',
                'id': '2'
            }
        ]

        jsonbands = json.dumps(bands)

        return render_to_response('base.html',
                                  {'bands': jsonbands},
                                  context_instance=RequestContext(request))