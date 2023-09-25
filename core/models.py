from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta


months = [
    (1, 'Enero'),
    (2, 'Febrero'),
    (3, 'Marzo'),
    (4, 'Abril'),
    (5, 'Mayo'),
    (6, 'Junio'),
    (7, 'Julio'),
    (8, 'Agosto'),
    (9, 'Septiembre'),
    (10, 'Octubre'),
    (11, 'Noviembre'),
    (12, 'Diciembre'),
]

class Customer(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombres', max_length = 50, unique = True)
    ip_address = models.CharField('IP', max_length = 15, unique = True)
    home_address = models.CharField('Dirección', max_length = 30, null=True, blank=True, default='')
    phone = models.CharField('Telefono', max_length = 10, null=True, blank=True, default='')
    month_payment = models.CharField('Pago mensual', max_length = 10, default = '0')
    mbps = models.CharField('Mbps', max_length = 10, default = '0')
    install_date = models.DateField('Fecha de instalación')
    is_active = models.BooleanField('Estado', default = True)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificación', auto_now=True)


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['name']
    
    def __str__(self):
        return str(self.name)


class Payment(models.Model):

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    month = models.SmallIntegerField('Mes', choices=months, default=int((date.today()-relativedelta(months=1)).strftime("%m")))
    year = models.CharField('Año',max_length=10, default=date.today().strftime("%Y"))
    amount = models.CharField('Monto', max_length=10, default='auto', blank=True)
    date = models.DateField('Fecha de pago', default=date.today)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificación', auto_now=True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['year','month']
    
    def __str__(self):
        return f'{self.customer.name}, {months[self.month-1][1]} {self.year} - {self.amount} soles'

    
    def save(self, *args, **kwargs):
        
        if (self.amount).replace(' ','')=='' or self.amount=='0' or self.amount=='Auto' or self.amount=='auto':
            customer = Customer.objects.get(pk=self.customer.id)
            self.amount = customer.month_payment               
            
        super(Payment, self).save(*args, **kwargs)


class History(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    action = models.CharField('Acción', max_length=20)
    date = models.DateField('Fecha')
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificación', auto_now=True)

    class Meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historial'
    
    def __str__(self):
        return f'{self.customer.name}, {self.action}, {self.date}'
