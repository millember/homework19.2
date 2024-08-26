from django.urls import path
import django.urls
from catalog import views

app_name = 'catalog'

urlpatterns = [

    django.urls.path('', views.index, name='index'),
    django.urls.path('', views.home, name='home'),
    django.urls.path('contact/', views.contact, name='contact'),

]
