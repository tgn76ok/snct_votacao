from django.db import models
from django.utils import timezone

class turmas(models.Model):
    imagem = models.ImageField(upload_to='grupimg/%Y/%m/%d')
    data_incricao = models.DateTimeField( default=timezone.now,editable=False)
    titulo = models.CharField(max_length=180)
    descricao = models.TextField(max_length=600)
    escola = models.CharField(max_length=180)
    tutor = models.CharField(max_length=180)
    integrantes =models.TextField()
    votos = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.titulo