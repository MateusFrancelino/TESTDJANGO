from django.db import models


class Campo(models.Model):
    
    nome = models.CharField(max_length = 255)
    descricao = models.CharField(max_length = 150, verbose_name = 'Descrição')

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

    def __unicode__(self):
        return 


class Atividade(models.Model):
    numero = models.IntegerField(verbose_name = 'Número')
    descricao = models.CharField(max_length = 150, verbose_name = 'Descrição')
    pontos = models.FloatField()
    detalhes = models.CharField(max_length = 100)

    campo = models.ForeignKey(Campo, on_delete = models.PROTECT)

    def __str__(self):
         return "{} - {} ({})".format(self.numero, self.descricao, self.campo.nome)

    def __unicode__(self):
        return 


class Status(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="descrição")

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)
    
class Classe(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.IntegerField(verbose_name="nível")
    descricao = models.CharField(max_length=150, verbose_name="descrição", null=True, blank=True)

    def __str__(self):
        return "{} nível {}".format(self.nome, self.nivel)
    
class Campus(models.Model):
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=150, verbose_name="endereço")
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)
    

