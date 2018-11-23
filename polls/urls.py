from django.urls import path

from . import views
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    #path('head', views.header, name='header'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('footer', views.footer, name='footer'),
    path('partners', views.partners, name='partners'),


]



