from django.contrib import admin
from .models import Selling

@admin.register(Selling)
class SellingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'price', 'house_type', 'image']
    list_filter = ['customer']
    ordering = ['customer']

fields = ( 'image_tag', )
readonly_fields = ('image_tag',)