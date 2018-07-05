from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
import datetime
from django.template import loader
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'Portalapp/index.html'
