from django.urls import path
from django.views.generic import TemplateView

from main import views


urlpatterns = [
    path('about-us/',
        TemplateView.as_view(template_name='main/about_us.html'),
        name='about_us'),
    path('contact-us/',
        views.ContactUsView.as_view(),
        name='contact_us'),
    path('products/<slug:tag>/',
        views.ProductListView.as_view(),
        name='products'),
    path('',
        TemplateView.as_view(template_name='main/home.html'),
        name='home'),
]
