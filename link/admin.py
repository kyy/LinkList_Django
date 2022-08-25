from django.contrib import admin

from .models import URL_list

@admin.register(URL_list)
class URL_listAdmin(admin.ModelAdmin):
    list_display = ['URL_short', 'name', 'URL_long', 'data']
    list_editable = ['name', 'URL_long']
    readonly_fields = ['data', 'URL_short']
    ordering = ['data', 'name']
    list_per_page = 5
