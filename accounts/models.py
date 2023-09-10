from django.db import models
from datetime import date

type_choices = [
    ('ingreso', 'Ingreso'),
    ('egreso', 'Egreso'),
]


# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    income = models.DecimalField('Ingreso Total', max_digits=6, decimal_places=2, default=0)
    expense = models.DecimalField('Egreso Total', max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField('Caja Total', max_digits=6, decimal_places=2, default=0)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Ultima actualización', auto_now=True)

    class Meta:
        verbose_name = 'Cuenta Total'
        verbose_name_plural = 'Cuenta Total'
    
    def __str__(self):
        return f'{self.total}'
    

# Create your models here.
class AccountItem(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, default=1, verbose_name='Cuenta')
    amount = models.DecimalField('Monto', max_digits=6, decimal_places=2)
    type = models.CharField('Ingreso / Egreso', max_length = 10, choices=type_choices,default='ingreso')
    details = models.CharField('Detalles', max_length=50, default='')
    date = models.DateField('Fecha', default=date.today)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Ultima actualización', auto_now=True)

    class Meta:
        verbose_name = 'Ingreso - Egreso'
        verbose_name_plural = 'Ingresos - Egresos'
    
    def __str__(self):
        return f'{self.date} {self.amount}'
    
    def save(self, *args, **kwargs):
        if self.type == 'ingreso':
            self.account.income += self.amount
            self.account.total += self.amount
        else:
            self.account.expense += self.amount
            self.account.total -= self.amount
        
        super().save(*args, **kwargs)
        self.account.save()
    