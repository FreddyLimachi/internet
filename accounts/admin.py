from django.contrib import admin
from accounts.models import Account, AccountItem
from django.utils.html import format_html
from django.conf import settings
from django import forms


class AccountItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'amount', 'details', 'date', 'edit')
    list_display_links = ('edit',)
    readonly_fields = ('created', 'updated')
    exclude = ('account',)
    list_per_page = 10
    
    def has_delete_permission(self, request, obj=None): return False
    def edit(self, obj):
        return format_html("<img src={icon_url}>", icon_url=settings.ICON_EDIT_URL)
    

    edit.short_description = '->'

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'income', 'expense', 'total', 'edit')
    list_display_links = ('edit',)
    readonly_fields = ('income', 'expense', 'total', 'created', 'updated')
    list_per_page = 10

    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False
    def edit(self, obj):
        return format_html("<img src={icon_url}>", icon_url=settings.ICON_EDIT_URL)

    edit.short_description = '->'


admin.site.register(Account, AccountAdmin)
admin.site.register(AccountItem, AccountItemAdmin)