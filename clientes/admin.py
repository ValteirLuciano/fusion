from django.contrib import admin
from .models import Cliente


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email', 'uf', 'cidade', 'endereco', 'imagem')


admin.site.register(Cliente, ClienteAdmin)
