from django.contrib import admin
from transfers.models import *

class TarifAdmin(admin.ModelAdmin):
    list_display = ('limit_inferior', 'limit_superior', 'montant')
    search_fields = ('montant',)
    ordering = ('montant',)

class TransferAdmin(admin.ModelAdmin):
    list_display = ('last_namesender', 'first_namesender','datedepot','villesender', 'montant','last_namereceiver', 'first_namereceiver','MTCN','datereceiver')
    search_fields = ('montant','villesender')
    ordering = ('montant','last_namesender','datereceiver','datedepot',)

admin.site.register(Tarif ,TarifAdmin)
admin.site.register(Transfert,TransferAdmin)
