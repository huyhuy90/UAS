from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('why', views.why, name='why'),
]