from django.contrib import admin
from shop.models import Category,Flavour,Occasion,Cake,CakeVarient,Order,OrderItems

# Register your models here.

admin.site.register(Category)
admin.site.register(Occasion)
admin.site.register(Flavour)
admin.site.register(Cake)
admin.site.register(CakeVarient)
admin.site.register(Order)
admin.site.register(OrderItems)