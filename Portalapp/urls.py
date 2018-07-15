from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'Portalapp'
urlpatterns = [

    path('', views.index, name='index'),
	path('guest/', views.guest, name='guest'),
	path('guest_ieee/', views.guest_ieee, name='guest_ieee'),
	path('guest_ie/', views.guest_ie, name='guest_ie'),
	path('guest_iet/', views.guest_iet, name='guest_iet'),
	path('guest_acm/', views.guest_acm, name='guest_acm'),
	path('guest_rotaract/', views.guest_rotaract, name='guest_rotaract'),
	path('guest_iste/', views.guest_iste, name='guest_iste'),
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