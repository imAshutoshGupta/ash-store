from django.urls import path
from ash_store import views

urlpatterns = [
    path('home',views.homepage),
    path('about',views.about),
    path('contact',views.contact),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('addition/<x>/<y>',views.addition),
    
]