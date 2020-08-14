from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Function_Images,Functions,Project_Images,Project,Exhibition,Exhibition_Images, Event
from BharatBhakti1 import settings
# Create your views here.

def homeview(request):

    try:
        events = Event.objects.all()

    except:
        return HttpResponse("Error while fetching Event database")

    return render(request, 'Home_html/index.html', {'events': events})

def projectlist(request):

    try:
        project_list = Project.objects.all()

        try:
            images = Project_Images.objects.filter(image_title="img")

        except:
            return HttpResponse("Error while reading project image database")

    except:
        return HttpResponse("Error while Project database")

    return render(request, 'Home_html/project/project_list_html.html', {"projects": project_list,
                                                                        "images": images})


def projectdetail(request, proj_name):

    try:
        project_details = Project_Images.objects.filter(project_name__project_title=proj_name)

    except:
        return HttpResponse("Error while Project database")

    return render(request, 'Home_html/project/project_detailed.html', {"project_details": project_details})


def programlist(request):

    try:
        function_list = Functions.objects.all()

        try:
            images = Function_Images.objects.filter(image_title="img")

        except:
            return HttpResponse("Error while reading Function image database")

    except:
        return HttpResponse("Error while Function database")

    return render(request, 'Home_html/program/program_list_html.html', {"functions": function_list,
                                                                        "images": images})


def programdetail(request, prog_name):

    try:
        function_details = Function_Images.objects.filter(function_name__function_title=prog_name)

    except:
        return HttpResponse("Error while function database")

    return render(request, 'Home_html/program/program_detailed.html', {"function_details": function_details})


def exhitionlist(request):

    try:
        exhibition_list = Exhibition.objects.all()

        try:
            images = Exhibition_Images.objects.filter(image_title="img")

        except:
            return HttpResponse("Error while reading Exhibition image database")

    except:
        return HttpResponse("Error while Exhibition database")

    return render(request, 'Home_html/exhibition/exhibition_list_html.html', {"exhibitions": exhibition_list,
                                                                                "images": images})


def exhitiondetail(request, exhib_name):

    try:
        exhibition_details = Exhibition_Images.objects.filter(exhibition_name__exhibition_title=exhib_name)

    except:
        return HttpResponse("Error while exhibition database")

    return render(request, 'Home_html/exhibition/exhibition_detailed.html', {"exhibition_details": exhibition_details})



def aboutUS(request):

    return render(request, 'Home_html/aboutBBS/about.html', {})


def aboutbabaji(request):

    return render(request, 'Home_html/aboutBBS/babaji.html', {})