from django import forms
from django.core.mail import send_mail
from django.conf import settings
#estudar ChoiceField
SERVICOS_CHOICES = (('Consultoria', 'Consultoria',), ('Capacitação', 'Capacitação',), ('Maximização de Lucros', 'Maximização de Lucros'))
class Contato(forms.Form):
	nome = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea) 
	telefone = forms.CharField(label='Telefone', max_length=11)
	servico = forms.ChoiceField(widget=forms.Select, choices=SERVICOS_CHOICES)

	def send_mail(self):
		subject = self.cleaned_data['nome']
		message = 'Nome: %(name)s; E-mail: %(email)s; %(message)s'
		context = {
			'nome': self.cleaned_data['nome'],
			'email': self.cleaned_data['email'],
			'message': self.cleaned_data['message'],
			'telefone': self.cleaned_data['telefone'],
			'servico': self.cleaned_data['servico'],
		}
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])