from django.contrib import admin
from .models import Customer, Payment, History
from django.utils.html import format_html
from django.conf import settings
from django import forms

class MyForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['month', 'year', 'date']
    
    """
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        if self.fields['amount'] == '70':
            print(self.fields['amount'])
            self.fields['month'].widget = forms.RadioSelect(choices=self.fields['month'].choices)
        else:
            print(self.fields['amount'])
            self.fields['month'].widget = forms.HiddenInput()
    
    """
    

class PaymentInline(admin.TabularInline):
    model = Payment
    form = MyForm
    extra = 2
    delete = False
    

class CustomerAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]
    readonly_fields = ('created','updated')
    list_display = ('payment', 'ip_address', 'mbps', 'is_active', 'edit')
    fields = ('name', 'ip_address', 'home_address', 'phone', 'month_payment', 'mbps', 'install_date', 'is_active')
    search_fields = ('name', 'ip_address')
    list_display_links = ('edit',)

    def payment(self, obj):
        return format_html("<a href='/admin/core/payment/?customer__name={slug}'>{name}</a>", slug=(obj.name).replace(' ', '+'), name=obj.name)

    def edit(self, obj):
        return format_html("<img src={icon_url}>", icon_url=settings.ICON_EDIT_URL)
    
    payment.short_description = 'Nombres'
    edit.short_description = '->'


class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('customer', 'month', 'year', 'amount', 'date', 'edit')
    exclude = ('amount',)
    list_filter = ('customer__name',)
    list_display_links = ('edit',)
    ordering = ['-year','-month']
    

    def edit(self, obj):
        return format_html("<img src={icon_url}>", icon_url=settings.ICON_EDIT_URL)
    
    edit.short_description = '->'


class HistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('customer', 'action', 'date')
    list_filter = ('customer__name','date')
    fields = ('customer', 'action', 'date')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(History, HistoryAdmin)