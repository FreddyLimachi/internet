from django.contrib import admin
from accounts.models import Account
from django.utils.html import format_html
from django.conf import settings
from django import forms


class AccountAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount', 'details', 'date', 'edit')
    readonly_fields = ('created','updated')
    list_display_links = ('edit',)

    def edit(self, obj):
        return format_html("<img src={icon_url}>", icon_url=settings.ICON_EDIT_URL)

    edit.short_description = '->'

admin.site.register(Account, AccountAdmin)