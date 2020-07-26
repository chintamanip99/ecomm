from django.contrib import admin
from .models import SellerProfile,CustomerProfile
# Register your models here.
admin.site.register(SellerProfile)
admin.site.register(CustomerProfile)