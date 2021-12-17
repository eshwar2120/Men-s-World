from django.contrib import admin
from .models import user_details,products,user_products
# Register your models here.
admin.site.register(user_details)
admin.site.register(products)
admin.site.register(user_products)