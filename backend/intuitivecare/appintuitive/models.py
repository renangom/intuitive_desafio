from django.db import models

# Create your models here.



class SCV(models.Model):
    RegistroANS = models.IntegerField(max_length=10)
    CNPJ = models.IntegerField(max_length=15)
    RazaoSocial = models.CharField(max_length=200)
    NomeFantasia = models.CharField(max_length=200)
    Modalidade = models.CharField(max_length=100)
    Logradouro = models.CharField(max_length=200)
    Numero = models.CharField(max_length=50)
    Complemento = models.CharField(max_length=200)
    Bairro = models.CharField(max_length=200)
    Cidade = models.CharField(max_length=200)
    UF = models.CharField(max_length=2)
    CEP = models.IntegerField(max_length=10)
    DDD = models.IntegerField(max_length=2)
    Telefone = models.IntegerField(max_length=15)
    Fax = models.IntegerField(max_length=15)
    Endereco = models.CharField(max_length=200)
    Representante = models.CharField(max_length=200)
    CargoRepresentante = models.CharField(max_length=200)
    DataRegistroANS = models.DateTimeField()