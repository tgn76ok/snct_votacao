from django.db import models
from django.utils import timezone

class escola(models.Model):
    name = models.CharField(max_length=180)
    def __str__(self):
        return self.name

class turmas(models.Model):
    data_incricao = models.DateTimeField( default=timezone.now,editable=False)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(max_length=600)
    email = models.CharField(max_length=200)
    nome_aplicativo = models.CharField(max_length=180)
    linkYoutube = models.CharField(max_length=180)
    arquivo_aplicativo = models.TextField(max_length=600)
    nome_equipe =  models.CharField(max_length=180)
    tutor = models.CharField(max_length=180)
    lider_equipe = models.CharField(max_length=180)
    integrantes =models.TextField()
    votos = models.PositiveIntegerField(default=0)

    escolaID = models.ForeignKey(escola,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo