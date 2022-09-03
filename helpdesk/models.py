from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=7, default='#000000')
    contador = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = "Status"
        ordering = ['nome']


class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = "Setores"


class Local(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = "Locais"
        ordering = ['nome']


class Solicitante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = "Solicitantes"
        ordering = ['nome']


class Person(User):
    class Meta:
        proxy = True
        ordering = ['first_name']
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.first_name


class Solicitacao(models.Model):
    descricao = models.TextField()
    usuario = models.ForeignKey(Person, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(
        Solicitante, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    patrimonio = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = "Solicitações"


class Resposta(models.Model):
    resposta = models.TextField(verbose_name='Resposta')
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.resposta
