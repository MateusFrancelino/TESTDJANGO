
# models.py
from django.db import models

class Nome(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Questao(models.Model):
    questao = models.CharField(max_length=50)

    def __str__(self):
        return self.questao

class Resposta(models.Model):
    nome_id = models.IntegerField()  # Chave estrangeira para a tabela Nome
    questao_id = models.IntegerField()  # Chave estrangeira para a tabela Questao
    alternativa = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.questao_id} - {self.nome_id}: {self.alternativa}"



# views.py
from django.shortcuts import render
from .models import Resposta, Nome, Questao

def tabela_respostas(request):
    # Obter todas as respostas
    respostas = Resposta.objects.all()

    # Inicializar um dicionário para armazenar as respostas no formato desejado
    respostas_formatadas = {}

    # Obter todas as questões únicas e todos os nomes únicos dos participantes
    questoes = Questao.objects.all()
    nomes = Nome.objects.all()

    # Processar as respostas e construir o dicionário
    for resposta in respostas:
        nome = Nome.objects.get(id=resposta.nome_id).nome
        questao = Questao.objects.get(id=resposta.questao_id).questao

        if nome not in respostas_formatadas:
            respostas_formatadas[nome] = {}

        respostas_formatadas[nome][questao] = resposta.alternativa

    # Passar os dados formatados para o template
    context = {
        'respostas': respostas_formatadas,
        'nomes': nomes,
        'questoes': questoes
    }

    return render(request, 'sua_template.html', context)
