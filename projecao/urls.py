"""projecao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from helpdesk.views import SolicitacaoCreateView, SolicitacaoDetailView, SolicitacaoUpdateView, SolicitacaoListView, SolicitacaoBusca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SolicitacaoListView.as_view()),
    path('solicitacao-add/', SolicitacaoCreateView.as_view(), name='solicitacao-add'),
    path('solicitacao-update/<int:pk>',
         SolicitacaoUpdateView.as_view(), name='solicitacao-update'),
    path('solicitacao-detail/<int:pk>',
         SolicitacaoDetailView.as_view(), name='solicitacao-detail'),
    path('busca/', SolicitacaoBusca.as_view(), name='solicitacao_busca'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
