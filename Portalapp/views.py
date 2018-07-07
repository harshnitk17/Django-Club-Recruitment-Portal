from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Clubinfo


def index(request):
    template = loader.get_template('Portalapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

