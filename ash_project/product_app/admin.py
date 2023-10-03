from django.contrib import admin
from .models import Product
# Register your models here.

#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):           #for customization of the product table in column names
    list_display=['name','price','qty','cat','is_available']        #empty list is defnined in ModelAdmin class, you just have to fill values
    list_filter=('cat','is_available')      #to use filters in sorting #can be used as tuple also
admin.site.register(Product,ProductAdmin)       #register in admin panel

#dash UI customization
admin.site.site_header="Ekart Dashboard"
admin.site.site_title="Ekart"