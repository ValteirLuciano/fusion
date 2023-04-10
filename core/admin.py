from django.contrib import admin
from .models import Cargo, Servico, Funcionario

# Register your models here.
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone', 'ativo', 'modificado')


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'bio', 'imagem', 'ativo', 'modificado')


admin.site.register(Cargo, CargoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
