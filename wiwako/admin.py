

# Register your models here.
from django.contrib import admin
from .models import Category, Wiwako,Submit
from carousel.models import CarouselItem



class WiwakoAdmin(admin.ModelAdmin):
    list_display = ['Eng_name', 'Geo_name', 'description', 'in_stock', 'Price', 'category']  
    list_filter = ['category', 'in_stock']  
    search_fields = ['Eng_name', 'Geo_name']  
    list_per_page = 20  



admin.site.register(Category)





@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'wiwako', 'get_redirect_url')
    readonly_fields = ('get_redirect_url',)



admin.site.register(Submit)