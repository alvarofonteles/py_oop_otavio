'''
Relações entre Classes
Associação - Python Orientado a Objetos - Aula 41
'''


# associação
class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None  # [1:1]
        self.__ferramentas = []  # [1:N]

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor

    # para a lista de ferramentas
    @property
    def ferramentas(self):
        return self.__ferramentas

    @ferramentas.setter
    def ferramenta(self, valor):
        self.__ferramentas = valor


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        return 'está escrevendo com a Caneta'


# com herança (futura aula)
class MaquinaDeEscrever(Caneta):
    '''Máquina de escrever'''

    # sobrescrita de método
    def escrever(self):
        return 'está escrevendo com a Máquina de escrever'


# extra associação (estudo a parte)
# objetos independentes colaborando
# outra forma usando o __str__ (acessa direto a instancia [print(produto) print(carrinho)])
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} - R$ {self.preco}'


class Carrinho:
    def __init__(self):
        self.produtos = []  # associação

    def __str__(self):
        produtos_str = '\n'.join([f'  - {produto}' for produto in self.produtos])
        return f'Carrinho com {len(self.produtos)} produtos:\n{produtos_str}'
