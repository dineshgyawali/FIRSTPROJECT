from django.contrib import admin
from .models import Customer, Staff, Support

# Register your models here.
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Support)