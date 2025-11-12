'''Métodos de Classes (@classmethod) - Python Orientado a Objetos - Aula 36'''

from datetime import datetime


class Animais:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def andar(self):
        return f'{self.nome} está andando'

    def get_ano_nasc(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        '''
        Método de classe - Construtor alternativo
        Cria instância a partir do ano de nascimento

        Args:
            nome (str): Nome do animal
            ano_nasc (int): Ano de nascimento

        Returns:
            Animais: Nova instância da classe Animais
        '''
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)
