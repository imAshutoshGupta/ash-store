from django.urls import path
from product_app import views

urlpatterns = [
    path('home',views.homepage),
    path('add_product',views.add_product),
    path('productdash', views.product_dashboard),
    path('delete/<pid>',views.delete_product),
    path('edit/<pid>',views.update_product),
]