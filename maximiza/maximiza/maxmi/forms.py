from django import forms
from django.core.mail import send_mail
from django.conf import settings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


SERVICOS_CHOICES = (('SERVIÇOS', 'SERVIÇOS',), ('Consultoria', 'Consultoria',), ('Capacitação', 'Capacitação',), ('Maximização de Lucros', 'Maximização de Lucros'))
class Contato(forms.Form):
	nome = forms.CharField(label='Nome', max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'NOME'}))
	telefone = forms.CharField(label='Telefone', max_length=11, widget=forms.TextInput(attrs={'placeholder': 'TELEFONE'}) )
	servico = forms.ChoiceField(widget=forms.Select() , choices=SERVICOS_CHOICES)
	email = forms.EmailField(label='E-mail',widget=forms.TextInput(attrs={'placeholder': 'E-MAIL'}) )
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'rows':5,'placeholder': 'MENSAGEM'})) 
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_show_labels = False

	def send_mail(self):
		subject = self.cleaned_data['nome']
		message = ' Nome: %(nome)s\n E-mail: %(email)s\n \n %(message)s \n %(servico)s'
		context = {
			'nome': self.cleaned_data['nome'],
			'email': self.cleaned_data['email'],
			'message': self.cleaned_data['message'],
			'telefone': self.cleaned_data['telefone'],
			'servico': self.cleaned_data['servico'],
			}
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])
