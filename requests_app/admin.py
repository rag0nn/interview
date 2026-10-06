from django.contrib import admin
from django.utils.text import Truncator

from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'description_preview', 'created_at']
    list_filter = ['service', 'created_at']
    search_fields = ['name', 'email', 'description']
    readonly_fields = ['created_at']

    @admin.display(description='Talep içeriği')
    def description_preview(self, obj):
        return Truncator(obj.description).chars(90)
