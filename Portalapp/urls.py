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

]