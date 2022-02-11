from django.contrib import admin
from .models import Product #.models means from current folde 
from .models import Offer

class ProductAdmin(admin.ModelAdmin):    #customizing Admin Area  ModelAdmin in admin model provides all functionality to manage Admin Area
    last_display = ('name', 'price', 'stock', 'image_url') #did not consider image_url as it could very long

class OfferAdmin(admin.ModelAdmin):
    last_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin) # we are telling django that we want to manage our product in the Admin Area and ProductAdmin
admin.site.register(Offer, OfferAdmin)