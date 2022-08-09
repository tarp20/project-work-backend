from django.contrib import admin

from leads.models import Lead


class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    search_fields = ['name', 'email']


admin.site.register(Lead, LeadAdmin)
