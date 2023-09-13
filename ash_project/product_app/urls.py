from django.urls import path
from product_app import views
urlpatterns = [
    path('home',views.homepage),
]