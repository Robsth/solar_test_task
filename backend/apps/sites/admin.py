from django.contrib import admin
from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('label', 'url', 'last_ping_date', 'availability_status')
    list_filter = ('availability_status',)
    search_fields = ('label', 'url')
    readonly_fields = ('availability_status', 'last_ping_date')
    ordering = ('label', 'availability_status')

