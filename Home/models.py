from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime

# Create your models here.
# ----------- Project Database --------- #


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=False)
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.project_title) + ", " + str(self.location)


def get_image_filename(instance, filename, *args, **kwargs):
    proj_folder = instance.project_name.project_title

    return "project_img/{folder}/{filename}".format(folder=proj_folder, filename=filename)


class Project_Images(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=100, blank=False, default="img")
    images = models.ImageField(upload_to=get_image_filename, blank=True, null=True)

    def __str__(self):
        return str(self.project_name.project_title) + ", " + str(self.image_title)


# ----------- Function Database --------- #


class Functions(models.Model):
    function_title = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=False)
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.function_title) + ", " + str(self.location)


def get_func_folder(instance, filename, *args, **kwargs):
    func_folder = instance.function_name.function_title

    return "function_img/{folder}/{filename}".format(folder=func_folder, filename=filename)


class Function_Images(models.Model):
    function_name = models.ForeignKey(Functions, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=100, blank=False, default="img")
    images = models.ImageField(upload_to=get_func_folder, blank=True, null=True)

    def __str__(self):
        return str(self.function_name.function_title) + ", " + str(self.image_title)


# ----------- Exhibition Database --------- #


class Exhibition(models.Model):
    exhibition_title = models.CharField(max_length=200)
    location = models.CharField(max_length=150, blank=False)
    description = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.exhibition_title) + ", " + str(self.location)


def get_exhib_folder(instance, filename, *args, **kwargs):
    exhib_folder = instance.exhibition_name.exhibition_title

    return "exhibition_img/{folder}/{filename}".format(folder=exhib_folder, filename=filename)


class Exhibition_Images(models.Model):
    exhibition_name = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=100, blank=False, default="img")
    images = models.ImageField(upload_to=get_exhib_folder, blank=True, null=True)

    def __str__(self):
        return str(self.exhibition_name.exhibition_title) + ", " + str(self.image_title)


# ----------- Event Database --------- #


class Event(models.Model):
    title = models.CharField(max_length=200, blank=False, default="Bharat Bhakti Sansthan")
    location = models.CharField(max_length=100, blank=False, default="Mumbai")
    event_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(self.title) + ", " + str(self.location)
