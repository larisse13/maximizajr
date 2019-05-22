from django.shortcuts import render
from django.http import HttpResponse
from .models import Quem_Somos, Portifolio, Servicos, Clientes,Banner
from .forms import Contato


def home(request):
  quemsomos = Quem_Somos.objects.last()
  portifolio = Portifolio.objects.all()
  servicos = Servicos.objects.all()
  clientes = Clientes.objects.all()
  banner = Banner.objects.all()
  context = {}
  if request.method =='POST':
    form = Contato(request.POST)
    if form.is_valid():
      context['is_valid']=True
      form.send_mail()
      print(form.cleaned_data)
      form = Contato()
  else:
    form = Contato()

  
  context['quemsomos'] = quemsomos
  context['portifolio'] = portifolio
  context['servicos'] = servicos
  context['clientes'] = clientes  
  context['form'] = form
  context['banner'] = banner 

  return render(request,'home.html', context)

