from django.urls import path
from Home import views

# TEMPLATE URLS!

app_name = 'Home'

urlpatterns = [

    path('', views.homeview, name='home'),

]
