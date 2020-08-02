from django.urls import path
from Home import views

# TEMPLATE URLS!

app_name = 'Home'

urlpatterns = [

    path('', views.homeview, name='home'),
    path('programlist', views.programlist, name='program'),
    path('projectlist', views.projectlist, name='project'),
    path('exhibitionlist', views.exhitionlist, name='exhibition'),
    path('about', views.aboutUS, name='about'),

]