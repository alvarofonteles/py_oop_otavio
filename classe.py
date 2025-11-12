'''
Classes - Python Orientado a Objetos - Aula 35.
'''

from datetime import datetime


class Pessoas:
    __ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.__nome = nome
        self.__idade = idade
        self.__comendo = comendo
        self.__falando = falando
        self.__alimento_atual = None
        self.__assunto_atual = None

    # método (API)
    def comer(self, alimento):
        if self.__comendo:
            self.__para_comer(self.__alimento_atual)

        if self.__falando:
            self.__para_falar(self.__assunto_atual)

        print(f'{self.__nome} {self.__idade}, está comendo {alimento}.')
        self.__comendo = True
        self.__alimento_atual = alimento

    # método (API)
    def falar(self, assunto):
        if self.__falando:
            self.__para_falar(self.__assunto_atual)

        if self.__comendo:
            self.__para_comer(self.__alimento_atual)

        print(f'{self.__nome} {self.__idade}, está falando sobre {assunto}')
        self.__falando = True
        self.__assunto_atual = assunto

    def __para_comer(self, alimento_atual):
        print(f'{self.__nome} parou de comer {alimento_atual}')
        self.__comendo = False
        self.__alimento_atual = None

    def __para_falar(self, assunto_atual):
        print(f'{self.__nome} parou de falar {assunto_atual}')
        self.__falando = False
        self.__assunto_atual = None

    # método (API)
    def get_dados(self):
        print(
            f'{self.__nome} tem {self.__idade} anos e está {f'saboerando {self.__alimento_atual}' if self.__comendo else f'discutindo sobre {self.__assunto_atual}'}'
        )

     # método (API)
    def get_nome(self):
        return self.__nome   

    # método (API)
    def get_ano_nasc(self):
        return self.__ano_atual - self.__idade


# Implementação para teste '__name__'
class Carros:
    def __init__(self, nome):
        self.nome = nome

    def correr(self):
        print(f'{self.nome} está correndo.')
