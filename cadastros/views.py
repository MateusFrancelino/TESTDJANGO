from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Campo, Atividade, Status, Classe, Campus


class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class ClasseCreate(CreateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class CampusCreate(CreateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')


#################### UPDATE ########################
class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class StatusUpdate(UpdateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class ClasseUpdate(UpdateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')

class CampusUpdate(UpdateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('inicio')




#################### DELETE ########################    
    
class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')

class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')

class StatusDelete(DeleteView):
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')

class ClasseDelete(DeleteView):
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')

class CampusDelete(DeleteView):
    model = Campus
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('inicio')

#################### LIST ########################    
    
class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'

class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'
