from django.contrib import admin

from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'created_at']
    list_filter = ['service', 'created_at']
    search_fields = ['name', 'email', 'description']
    readonly_fields = ['created_at']
