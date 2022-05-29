from django.db import models
from django.db import models

# Importe a classe que apresentará um erro de validação
from django.core.exceptions import ValidationError

# Crie um método para validar o valor informado


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('O CPF deve conter apenas números')


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11, validators=[validate_cpf])
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):

    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')






