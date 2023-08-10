from django.contrib import admin
from .models import Customer, Payment, History
from django.utils.html import format_html
from django.conf import settings
from django import forms
from django.http import HttpResponse
import csv



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
    extra = 1
    delete = False
    

class CustomerAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]
    list_per_page = 10
    readonly_fields = ('created','updated')
    list_display = ('payment', 'ip_address', 'mbps', 'is_active', 'edit')
    fields = ('name', 'ip_address', 'home_address', 'phone', 'month_payment', 'mbps', 'install_date', 'is_active')
    search_fields = ('name', 'ip_address')
    list_display_links = ('edit',)
    actions = ['export_to_csv']
    list_per_page = 10

    def payment(self, obj):
        return format_html("<a href='/admin/core/payment/?customer__name={slug}'>{name}</a>", slug=(obj.name).replace(' ', '+'), name=obj.name)

    def edit(self, obj):
        return format_html("<img src={icon_url}>", icon_url=settings.ICON_EDIT_URL)
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="datos_exportados.csv"'
        writer = csv.writer(response)
        writer.writerow([field.name for field in queryset.model._meta.fields])

        for obj in queryset:
            writer.writerow([getattr(obj, field.name) for field in queryset.model._meta.fields])
        
        return response
    
    payment.short_description = 'Nombres'
    edit.short_description = '->'
    export_to_csv.short_description = 'Exportar en CSV'


class PaymentAdmin(admin.ModelAdmin):
    list_per_page = 10
    readonly_fields = ('created','updated')
    list_display = ('customer', 'month', 'year', 'amount', 'date', 'edit')
    exclude = ('amount',)
    list_filter = ('customer__name',)
    list_display_links = ('edit',)
    ordering = ['-year','-month']
    actions = ['export_to_csv']
    list_per_page = 10

    def edit(self, obj):
        return format_html("<img src={icon_url}>", icon_url=settings.ICON_EDIT_URL)
    
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="datos_exportados.csv"'
        writer = csv.writer(response)
        writer.writerow([field.name for field in queryset.model._meta.fields])

        for obj in queryset:
            writer.writerow([getattr(obj, field.name) for field in queryset.model._meta.fields])
        
        return response
    
    edit.short_description = '->'
    export_to_csv.short_description = 'Exportar en CSV'


class HistoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    readonly_fields = ('created','updated')
    list_display = ('customer', 'action', 'date')
    list_filter = ('customer__name','date')
    fields = ('customer', 'action', 'date')
    actions = ['export_to_csv']
    list_per_page = 10

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="datos_exportados.csv"'
        writer = csv.writer(response)
        writer.writerow([field.name for field in queryset.model._meta.fields])

        for obj in queryset:
            writer.writerow([getattr(obj, field.name) for field in queryset.model._meta.fields])
        
        return response
    
    export_to_csv.short_description = 'Exportar en CSV'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(History, HistoryAdmin)