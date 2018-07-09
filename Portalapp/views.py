from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.template import loader

from .models import Clubinfo,form
from .forms import ApplicationForm



def index(request):
    template = loader.get_template('Portalapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ieee(request):
    club_name="IEEE"
    club_info = get_object_or_404(Clubinfo, pk=1).club_text
    ''' club_logo= get_object_or_404(Clubinfo, pk=1).image'''
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')
    else:
        f = ApplicationForm()
    
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,}
    return HttpResponse(template.render(context, request))
def acm(request):
    club_name="ACM"
    club_info = get_object_or_404(Clubinfo, pk=2).club_text
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,}
    return HttpResponse(template.render(context, request))
def rotaract(request):
    club_name="Rotaract"
    club_info = get_object_or_404(Clubinfo, pk=3).club_text
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,}
    return HttpResponse(template.render(context, request))
def iste(request):
    club_name="ISTE"
    club_info = get_object_or_404(Clubinfo, pk=5).club_text
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,}
    return HttpResponse(template.render(context, request))
def ie(request):
    club_name="IE"
    club_info = get_object_or_404(Clubinfo, pk=4).club_text
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,}
    return HttpResponse(template.render(context, request))
def iet(request):
    club_name="IET"
    club_info = get_object_or_404(Clubinfo, pk=6).club_text
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,}
    return HttpResponse(template.render(context, request))
def confirmation(request):
    template = loader.get_template('Portalapp/sub/information.html')
    context = {}
    return HttpResponse(template.render(context, request))