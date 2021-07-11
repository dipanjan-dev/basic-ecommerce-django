from django.contrib import admin
from .models import product , Contact , Order


class products(admin.ModelAdmin):
     list_display = ('product_name','product_category','product_price','product_date')
     list_per_page = 15
     search_fields = ('product_name','product_category')
     list_filter = ('product_category','product_price','product_date')

class Contacts(admin.ModelAdmin):
     list_display = ('name','phone','email')
     list_per_page = 15
     search_fields = ('name','email','phone')
     
class Customer(admin.ModelAdmin):
     list_display = ('name','phone','email','address','order_product','price')
     list_per_page = 15
     search_fields = ('name','email','phone','order_product')
     list_filter = ('order_product',)


# Register your models here.

admin.site.register(product,products)
admin.site.register(Contact,Contacts)
admin.site.register(Order,Customer)
