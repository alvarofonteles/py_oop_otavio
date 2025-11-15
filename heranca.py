'''
Relações entre Classes
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É

Herança simples - Python Orientado a Objetos - Aula 44
'''


# estrutura simples, apenas didático
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_class = self.__class__.__name__

    def falando(self):
        print(f'{self.nome_class} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_class} está comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_class} está estudando...')
