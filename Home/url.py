from django.urls import path
from Home import views
from BharatBhakti1 import settings
from django.conf.urls.static import static

# TEMPLATE URLS!

app_name = 'Home'

urlpatterns = [

    path('', views.homeview, name='home'),
    path('programlist/', views.programlist, name='program'),
    path('programdetail/<str:prog_name>/', views.programdetail, name='programdetail'),
    path('projectlist/', views.projectlist, name='project'),
    path('projectdetail/<str:proj_name>/', views.projectdetail, name='projectdetail'),
    path('exhibitionlist/', views.exhitionlist, name='exhibition'),
    path('exhibitiondetail/<str:exhib_name>/', views.exhitiondetail, name='exhibitiondetail'),
    path('about/', views.aboutUS, name='about'),
    path('aboutbabaji/', views.aboutbabaji, name='aboutbabaji'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
