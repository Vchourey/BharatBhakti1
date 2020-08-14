from django.contrib import admin
from .models import Project_Images, Project, Function_Images, Functions, Exhibition, Exhibition_Images, Event
# Register your models here.


class Event_Admin(admin.ModelAdmin):


    # list of fields to display in django admin

    list_display = ['id', 'title', 'location']


admin.site.register(Project)
admin.site.register(Project_Images)
admin.site.register(Functions)
admin.site.register(Function_Images)
admin.site.register(Exhibition)
admin.site.register(Exhibition_Images)
admin.site.register(Event, Event_Admin)
