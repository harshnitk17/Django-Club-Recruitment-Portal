from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'Portalapp'
urlpatterns = [

    path('', views.index, name='index'),
	path('ieee/', views.ieee, name='ieee'),
	path('acm/', views.acm, name='acm'),
	path('rotaract/', views.rotaract, name='rotaract'),
	path('iste/', views.iste, name='iste'),
	path('ie/', views.ie, name='ie'),
	path('iet/', views.iet, name='iet'),
	path('confirmation/', views.confirmation, name='confirmation'),
    path('Admin/', views.Admin, name='Admin'),
	path('adminsite_ieee/', views.adminsite_ieee, name='adminsite_ieee'),
	path('adminsite_ie/', views.adminsite_ie, name='adminsite_ie'),
	path('adminsite_iet/', views.adminsite_iet, name='adminsite_iet'),
	path('adminsite_acm/', views.adminsite_acm, name='adminsite_acm'),
	path('adminsite_rotaract/', views.adminsite_rotaract, name='adminsite_rotaract'),
	path('adminsite_iste/', views.adminsite_iste, name='adminsite_iste'),
	path('approval_ieee/', views.approval_ieee, name='approval_ieee'),
	path('approval_ie/', views.approval_ie, name='approval_ie'),
	path('approval_iet/', views.approval_iet, name='approval_iet'),
	path('approval_acm/', views.approval_acm, name='approval_acm'),
	path('approval_iste/', views.approval_iste, name='approval_iste'),
	path('approval_rotaract/', views.approval_rotaract, name='approval_rotaract'),

]