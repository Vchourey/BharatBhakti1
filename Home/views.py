from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def homeview(request):

    return render(request, 'Home_html/index.html', {})

def projectlist(request):

    return render(request, 'Home_html/project/project_list_html.html', {})

def programlist(request):

    return render(request, 'Home_html/program/program_list_html.html', {})

def exhitionlist(request):

    return render(request, 'Home_html/exhibition/exhibition_list_html.html', {})

def aboutUS(request):

    return render(request, 'Home_html/aboutBBS/about.html', {})
