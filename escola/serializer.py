from rest_framework import serializers
from .models import Curso, Aluno, Matricula


class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aluno
        #extra_kwargs = {
        #    'cpf': {'write_only': True}
        #}
        fields = (
            'id',
            'nome',
            'rg',
            'cpf',
            'data_nascimento',
        )


class CursoSerializer(serializers.ModelSerializer):
    
    nivel = serializers.SerializerMethodField()

    def get_nivel(self, obj):
        return obj.get_nivel_display()

    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    periodo = serializers.SerializerMethodField()

    def get_periodo(self, obj):
        return obj.get_periodo_display()

    class Meta:
        model = Matricula
        fields = '__all__'


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    # Para trazer o nome da descricao do curso #
    curso = serializers.ReadOnlyField(source='curso.descricao')
    # Para trazer algo de multipla escolha #
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno_nome']

