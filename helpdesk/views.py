from re import template
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RespostaForm, SolicitacaoForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic import FormView
from helpdesk.models import Resposta, Solicitacao
from helpdesk.models import Status
from django.contrib import messages
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count, Case, When


class SolicitacaoCreateView(LoginRequiredMixin, CreateView):
    model = Solicitacao
    fields = ('descricao', 'usuario', 'local',
              'solicitante', 'status', 'patrimonio')
    template_name = 'solicitacao.html'
    success_url = '/'
    login_url = 'accounts/login/'


class SolicitacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Solicitacao
    form_class = SolicitacaoForm
    template_name = 'solicitacao-update.html'
    success_url = '/'
    login_url = 'accounts/login/'

    solicitacao_form = SolicitacaoForm()
    resposta_form = RespostaForm()


class SolicitacaoListView(LoginRequiredMixin, ListView):
    model = Solicitacao
    ordering = ['-data_criacao']
    login_url = 'accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'status_list': Status.objects.all().order_by('id')
        })

        context['solictacao_total'] = Solicitacao.objects.filter().count()
        return context


class SolicitacaoDetailView(LoginRequiredMixin, SingleObjectMixin, FormView):
    model = Solicitacao
    template_name = 'solicitacao-detail.html'
    form_class = RespostaForm
    login_url = 'accounts/login/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Solicitacao.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solicitacao'] = self.object
        context['resposta_form'] = RespostaForm()
        context['respostas'] = Resposta.objects.filter(solicitacao=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Solicitacao.objects.all())
        form = self.get_form()
        resposta = form.save(commit=False)

        if request.user.is_authenticated:
            resposta.usuario = request.user
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        resposta = form.save(commit=False)
        resposta.solicitacao = self.object
        resposta.save()
        messages.success(self.request, 'Resposta enviada com sucesso!')
        return redirect(reverse('solicitacao-detail', kwargs={'pk': self.object.id}))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SolicitacaoBusca(SolicitacaoListView):
    template_name = 'solicitacao_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        if not termo:
            return qs

        qs = qs.filter(
            Q(descricao__icontains=termo) |
            Q(usuario__first_name__iexact=termo) |
            Q(patrimonio__icontains=termo) |
            Q(local__nome__iexact=termo) |
            Q(solicitante__nome__iexact=termo) |
            Q(status__nome__iexact=termo)
        )

        return qs
