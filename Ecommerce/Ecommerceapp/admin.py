from django.contrib import admin

# Register your models here.
from .models import Users, Address, Productdetails, Producttype, Orderdetails, Orderconfirm, Deliverydetails, Cartitems, Productimages, ProductReviews
admin.site.register(Users)
admin.site.register(Address)
admin.site.register(Productdetails)
admin.site.register(Producttype)
admin.site.register(Orderdetails)
admin.site.register(Orderconfirm)
admin.site.register(Deliverydetails)
admin.site.register(Cartitems)
admin.site.register(Productimages)
admin.site.register(ProductReviews)