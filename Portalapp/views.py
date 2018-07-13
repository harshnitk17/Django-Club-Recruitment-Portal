from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.template import loader

from .models import Clubinfo,form,admin,form2
from .forms import ApplicationForm,AdminForm,form21



def index(request):
    template = loader.get_template('Portalapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def ieee(request):
    club_name="IEEE"
    club_info = get_object_or_404(Clubinfo, pk=1).club_text
    image= get_object_or_404(Clubinfo, pk=1).image
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')
    else:
        f = ApplicationForm()
    
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,'image_url':image,}
    return HttpResponse(template.render(context, request))
def acm(request):
    club_name="ACM"
    club_info = get_object_or_404(Clubinfo, pk=2).club_text
    image= get_object_or_404(Clubinfo, pk=2).image
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,'image_url':image,}
    return HttpResponse(template.render(context, request))
def rotaract(request):
    club_name="Rotaract"
    club_info = get_object_or_404(Clubinfo, pk=3).club_text
    image= get_object_or_404(Clubinfo, pk=3).image
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,'image_url':image,}
    return HttpResponse(template.render(context, request))
def iste(request):
    club_name="ISTE"
    club_info = get_object_or_404(Clubinfo, pk=5).club_text
    image= get_object_or_404(Clubinfo, pk=5).image
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,'image_url':image,}
    return HttpResponse(template.render(context, request))
def ie(request):
    club_name="IE"
    club_info = get_object_or_404(Clubinfo, pk=4).club_text
    image= get_object_or_404(Clubinfo, pk=4).image
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,'image_url':image,}
    return HttpResponse(template.render(context, request))
def iet(request):
    club_name="IET"
    club_info = get_object_or_404(Clubinfo, pk=6).club_text
    image= get_object_or_404(Clubinfo, pk=6).image
    if request.POST:
        f = ApplicationForm(request.POST)
        if f.is_valid():
            entry = f.save()
            return redirect('Portalapp:confirmation')

    else:
        f = ApplicationForm()
    template = loader.get_template('Portalapp/sub/club.html')
    context = {'club':club_name,'Clubinformation':club_info,'form':f,'image_url':image,}
    return HttpResponse(template.render(context, request))
def confirmation(request):
    template = loader.get_template('Portalapp/sub/information.html')
    context = {}
    return HttpResponse(template.render(context, request))
def Admin(request):
    error=""
    if request.POST:
        f=AdminForm(request.POST)
        if f.is_valid():
            q= get_object_or_404(admin, club_name=f.cleaned_data['club_name'])
            if f.cleaned_data['user_name']==q.user_name :
                if f.cleaned_data['password']==q.password :
                    if f.cleaned_data['club_name']=="IEEE":
                        return HttpResponseRedirect(reverse('Portalapp:adminsite_ieee'))
                    elif f.cleaned_data['club_name']=="IET":
                        return HttpResponseRedirect(reverse('Portalapp:adminsite_iet'))
                    elif f.cleaned_data['club_name']=="IE":
                        return HttpResponseRedirect(reverse('Portalapp:adminsite_ie'))
                    elif f.cleaned_data['club_name']=="ACM":
                        return HttpResponseRedirect(reverse('Portalapp:adminsite_acm'))
                    elif f.cleaned_data['club_name']=="ROTARACT":
                        return HttpResponseRedirect(reverse('Portalapp:adminsite_rotaract'))
                    elif f.cleaned_data['club_name']=="ISTE":
                        return HttpResponseRedirect(reverse('Portalapp:adminsite_iste'))
                    
                else:
                    error="Password is incorrect"
                    template = loader.get_template('Portalapp/sub/admin.html')
                    context = {'error':error,'form':f,}
                    return HttpResponse(template.render(context, request))
            else:
                error="Username is incorrect"
                template = loader.get_template('Portalapp/sub/admin.html')
                context = {'error':error,'form':f,}
                return HttpResponse(template.render(context, request))
    else:
        f=AdminForm()
    template = loader.get_template('Portalapp/sub/admin.html')
    context = {'error':error,'form':f,}
    return HttpResponse(template.render(context, request))

def adminsite_ieee(request):
    template = loader.get_template('Portalapp/sub/adminsite.html')
    club_name="IEEE"
    names=form.objects.values_list('name', flat=True).filter(club=club_name,approval=False)
    branch=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=False)
    roll_number=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=False)
    date=form.objects.values_list('date', flat=True).filter(club=club_name,approval=False)
    info=form.objects.values_list('info', flat=True).filter(club=club_name,approval=False)
    email=form.objects.values_list('email', flat=True).filter(club=club_name,approval=False)
    phone=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=False)
    approval=form.objects.values_list('approval', flat=True).filter(club=club_name,approval=False)
    names_n=form.objects.values_list('name', flat=True).filter(club=club_name,approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(club=club_name,approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(club=club_name,approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(club=club_name,approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=True)
    
    if request.POST:
        l=request.POST.getlist('approval')
        for i in range(len(l)):
            a=form2(approval=l[i])
            a.save()
        return redirect('Portalapp:approval_ieee')

    context = {'club_name':club_name,'name':names,'branch':branch,'roll_number':roll_number,'date':date,'info':info,'email':email,'phone':phone,'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))
	
def adminsite_ie(request):
    template = loader.get_template('Portalapp/sub/adminsite.html')
    club_name="IE"
    names=form.objects.values_list('name', flat=True).filter(club=club_name,approval=False)
    branch=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=False)
    roll_number=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=False)
    date=form.objects.values_list('date', flat=True).filter(club=club_name,approval=False)
    info=form.objects.values_list('info', flat=True).filter(club=club_name,approval=False)
    email=form.objects.values_list('email', flat=True).filter(club=club_name,approval=False)
    phone=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=False)
    approval=form.objects.values_list('approval', flat=True).filter(club=club_name,approval=False)
    names_n=form.objects.values_list('name', flat=True).filter(club=club_name,approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(club=club_name,approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(club=club_name,approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(club=club_name,approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=True)
    
    if request.POST:
        l=request.POST.getlist('approval')
        for i in range(len(l)):
            a=form2(approval=l[i])
            a.save()
        return redirect('Portalapp:approval_ie')

    context = {'club_name':club_name,'name':names,'branch':branch,'roll_number':roll_number,'date':date,'info':info,'email':email,'phone':phone,'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))
def adminsite_iet(request):
    template = loader.get_template('Portalapp/sub/adminsite.html')
    club_name="IET"
    names=form.objects.values_list('name', flat=True).filter(club=club_name,approval=False)
    branch=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=False)
    roll_number=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=False)
    date=form.objects.values_list('date', flat=True).filter(club=club_name,approval=False)
    info=form.objects.values_list('info', flat=True).filter(club=club_name,approval=False)
    email=form.objects.values_list('email', flat=True).filter(club=club_name,approval=False)
    phone=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=False)
    approval=form.objects.values_list('approval', flat=True).filter(club=club_name,approval=False)
    names_n=form.objects.values_list('name', flat=True).filter(club=club_name,approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(club=club_name,approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(club=club_name,approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(club=club_name,approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=True)
    
    if request.POST:
        l=request.POST.getlist('approval')
        for i in range(len(l)):
            a=form2(approval=l[i])
            a.save()
        return redirect('Portalapp:approval_iet')

    context = {'club_name':club_name,'name':names,'branch':branch,'roll_number':roll_number,'date':date,'info':info,'email':email,'phone':phone,'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))
def adminsite_acm(request):
    template = loader.get_template('Portalapp/sub/adminsite.html')
    club_name="ACM"
    names=form.objects.values_list('name', flat=True).filter(club=club_name,approval=False)
    branch=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=False)
    roll_number=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=False)
    date=form.objects.values_list('date', flat=True).filter(club=club_name,approval=False)
    info=form.objects.values_list('info', flat=True).filter(club=club_name,approval=False)
    email=form.objects.values_list('email', flat=True).filter(club=club_name,approval=False)
    phone=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=False)
    approval=form.objects.values_list('approval', flat=True).filter(club=club_name,approval=False)
    names_n=form.objects.values_list('name', flat=True).filter(club=club_name,approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(club=club_name,approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(club=club_name,approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(club=club_name,approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=True)
    
    if request.POST:
        l=request.POST.getlist('approval')
        for i in range(len(l)):
            a=form2(approval=l[i])
            a.save()
        return redirect('Portalapp:approval_acm')

    context = {'club_name':club_name,'name':names,'branch':branch,'roll_number':roll_number,'date':date,'info':info,'email':email,'phone':phone,'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))
def adminsite_rotaract(request):
    template = loader.get_template('Portalapp/sub/adminsite.html')
    club_name="ROTARACT"
    names=form.objects.values_list('name', flat=True).filter(club=club_name,approval=False)
    branch=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=False)
    roll_number=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=False)
    date=form.objects.values_list('date', flat=True).filter(club=club_name,approval=False)
    info=form.objects.values_list('info', flat=True).filter(club=club_name,approval=False)
    email=form.objects.values_list('email', flat=True).filter(club=club_name,approval=False)
    phone=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=False)
    approval=form.objects.values_list('approval', flat=True).filter(club=club_name,approval=False)
    names_n=form.objects.values_list('name', flat=True).filter(club=club_name,approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(club=club_name,approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(club=club_name,approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(club=club_name,approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=True)
    
    if request.POST:
        l=request.POST.getlist('approval')
        for i in range(len(l)):
            a=form2(approval=l[i])
            a.save()
        return redirect('Portalapp:approval_rotaract')

    context = {'club_name':club_name,'name':names,'branch':branch,'roll_number':roll_number,'date':date,'info':info,'email':email,'phone':phone,'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))
def adminsite_iste(request):
    template = loader.get_template('Portalapp/sub/adminsite.html')
    club_name="ISTE"
    names=form.objects.values_list('name', flat=True).filter(club=club_name,approval=False)
    branch=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=False)
    roll_number=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=False)
    date=form.objects.values_list('date', flat=True).filter(club=club_name,approval=False)
    info=form.objects.values_list('info', flat=True).filter(club=club_name,approval=False)
    email=form.objects.values_list('email', flat=True).filter(club=club_name,approval=False)
    phone=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=False)
    approval=form.objects.values_list('approval', flat=True).filter(club=club_name,approval=False)
    names_n=form.objects.values_list('name', flat=True).filter(club=club_name,approval=True)
    branch_n=form.objects.values_list('branch', flat=True).filter(club=club_name,approval=True)
    roll_number_n=form.objects.values_list('roll_number', flat=True).filter(club=club_name,approval=True)
    date_n=form.objects.values_list('date', flat=True).filter(club=club_name,approval=True)
    info_n=form.objects.values_list('info', flat=True).filter(club=club_name,approval=True)
    email_n=form.objects.values_list('email', flat=True).filter(club=club_name,approval=True)
    phone_n=form.objects.values_list('phone', flat=True).filter(club=club_name,approval=True)
    
    if request.POST:
        l=request.POST.getlist('approval')
        for i in range(len(l)):
            a=form2(approval=l[i])
            a.save()
        return redirect('Portalapp:approval_iste')

    context = {'club_name':club_name,'name':names,'branch':branch,'roll_number':roll_number,'date':date,'info':info,'email':email,'phone':phone,'approval':approval,'name_n':names_n,'branch_n':branch_n,'roll_number_n':roll_number_n,'date_n':date_n,'info_n':info_n,'email_n':email_n,'phone_n':phone_n,}
    return HttpResponse(template.render(context, request))
def approval_ieee(request):
    roll_number=form2.objects.values_list('approval', flat=True)
    for i in roll_number:
        q=get_object_or_404(form, roll_number=i)
        q.approval=1
        q.save()
    return redirect('Portalapp:adminsite_ieee')
def approval_ie(request):
    roll_number=form2.objects.values_list('approval', flat=True)
    for i in roll_number:
        q=get_object_or_404(form, roll_number=i)
        q.approval=1
        q.save()
    return redirect('Portalapp:adminsite_ie')	
def approval_iet(request):
    roll_number=form2.objects.values_list('approval', flat=True)
    for i in roll_number:
        q=get_object_or_404(form, roll_number=i)
        q.approval=1
        q.save()
    return redirect('Portalapp:adminsite_iet')
def approval_iste(request):
    roll_number=form2.objects.values_list('approval', flat=True)
    for i in roll_number:
        q=get_object_or_404(form, roll_number=i)
        q.approval=1
        q.save()
    return redirect('Portalapp:adminsite_iste')   
def approval_acm(request):
    roll_number=form2.objects.values_list('approval', flat=True)
    for i in roll_number:
        q=get_object_or_404(form, roll_number=i)
        q.approval=1
        q.save()
    return redirect('Portalapp:adminsite_acm')
def approval_rotaract(request):
    roll_number=form2.objects.values_list('approval', flat=True)
    for i in roll_number:
        q=get_object_or_404(form, roll_number=i)
        q.approval=1
        q.save()
    return redirect('Portalapp:adminsite_rotaract')