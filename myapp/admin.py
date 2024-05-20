from django.contrib import admin
from .models import Application, ClientInfo, CreditPay, CreditPayment, AddClients
# Register your models here.

admin.site.register(Application)
admin.site.register(ClientInfo)
admin.site.register(CreditPay)
admin.site.register(CreditPayment)
admin.site.register(AddClients)
