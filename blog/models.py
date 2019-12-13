from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=70, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    data_cadastro = models.DateField(auto_now_add=True)
    data_edicao = models.DateField(auto_now=True)
    categoria = models.ManyToManyField(Categoria)
    capa = models.ImageField(upload_to='artigos/', null=True)

    def __str__(self):
        return self.titulo
