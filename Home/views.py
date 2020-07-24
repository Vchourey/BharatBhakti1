from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def homeview(request):

    return render(request, 'Home_html/index.html', {})