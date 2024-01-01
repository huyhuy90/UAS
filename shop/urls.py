from django.urls import path
from . import views 
from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop, name='shop'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('why', views.why, name='why'),
    path('siwil', views.siwil, name='siwil'),  
    path('addnew',views.addnew, name='addnew'),  
    path('edit/<int:id>', views.edit, name='edit'),  
    path('update/<int:id>', views.update, name='update'),  
    path('delete/<int:id>', views.destroy, name='destroy'),  
]