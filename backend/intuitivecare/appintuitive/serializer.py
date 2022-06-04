from rest_framework import serializers
from .models import *

class SCVSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SCV
        fields = ['url','RegistroANS','CNPJ', 'RazaoSocial', 'NomeFantasia', 'Modalidade','Logradouro', 'Numero',
        'Complemento','Bairro', 'Cidade', 'UF', 'CEP', 'DDD', 'Telefone', 'Fax', 'Endereco', 'Representante',
        'CargoRepresentante', 'DataRegistroANS']