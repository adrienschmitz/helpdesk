from urllib import request
from django import forms
from django.forms import ModelForm, Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button
from crispy_forms.bootstrap import FormActions
from helpdesk.models import Resposta, Solicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ('descricao', 'usuario', 'solicitante',
                  'local', 'patrimonio', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.add_input(Submit('submit', 'Salvar', css_class='btn-success'))
        self.helper.layout = Layout(
            Row(
                Column('descricao', css_class='form-group col-md-12 mb-0'),

            ),
            Row(
                Column('solicitante', css_class='form-group col-md-6 mb-0'),
                Column('usuario', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('local', css_class='form-group col-md-6 mb-0'),
                Column('patrimonio', css_class='form-group col-md-6 mb-0'),
            ),
            Row(
                Column('status', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit_solicitacao', 'Salvar', css_class='btn-success')
        )


class RespostaForm(ModelForm):

    class Meta:
        model = Resposta
        fields = ('resposta',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.fields['resposta'].widget.attrs['rows'] = 5
        self.helper.form_show_labels = False
        self.helper.layout = Layout(

            Row(
                Column('resposta', rows='2',
                       css_class='form-group col-md-12 mb-0'),

            ),
            Submit('submit_resposta', 'Salvar', css_class='btn-success'),
        )
