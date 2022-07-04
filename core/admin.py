from django.contrib import admin
from .models import Customer, Payment, History


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name', 'ip_address', 'mbps', 'is_active')
    fields = ('name', 'ip_address', 'home_address', 'phone', 'month_payment', 'mbps', 'install_date', 'is_active')
    search_fields = ('name', 'ip_address')

class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('customer', 'month', 'year', 'amount', 'date')
    list_filter = ('customer__name','year','month')
    fields = ('customer', 'month', 'year', 'amount', 'date', 'created', 'updated')

class HistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('customer', 'action', 'date')
    list_filter = ('customer__name','date')
    fields = ('customer', 'action', 'date')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(History, HistoryAdmin)