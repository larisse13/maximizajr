from django import forms
from django.core.mail import send_mail
from django.conf import settings
#estudar ChoiceField
class Contato(forms.Form):
	nome = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail')
	message = forms.CharField(label='Mensagem', widget=forms.Textarea) 
	telefone = forms.CharField(label='Telefone', max_length=11)

	def send_mail(self):
		subject = self.cleaned_data['nome']
		message = 'Nome: %(name)s; E-mail: %(email)s; %(message)s'
		context = {
			'nome': self.cleaned_data['nome']
			'email': self.cleaned_data['email']
			'message': self.cleaned_data['message']
			'telefone': self.cleaned_data['telefone']
		}
		message = message % context
		send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])