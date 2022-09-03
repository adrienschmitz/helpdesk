from django.contrib import admin
from .models import Solicitante, Solicitacao,  Setor, Local, Status, Resposta


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cor', 'contador')
    list_editable = ('contador',)


class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor')


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'usuario', 'data_criacao',
                    'data_atualizacao', 'status')


class RespostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data')


admin.site.register(Status, StatusAdmin)
admin.site.register(Solicitante, SolicitanteAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Solicitacao, SolicitacaoAdmin)
admin.site.register(Resposta, RespostaAdmin)
