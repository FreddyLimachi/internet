from django.db import models
from simple_history.models import HistoricalRecords
from datetime import date

type_choices = [
    ('ingreso', 'Ingreso'),
    ('egreso', 'Egreso'),
]


# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.DecimalField('Pago', max_digits=6, decimal_places=2, choices=type_choices)
    type = models.CharField('Ingreso / Egreso', max_length = 10, default='ingreso')
    details = models.CharField('Detalles', max_length=50, default='')
    date = models.DateField('Fecha', default=date.today)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de modificación', auto_now=True)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
    
    def __str__(self):
        return f'{self.date} {self.amount}'
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value