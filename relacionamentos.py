'''
Relações entre Classes
Associação - Python Orientado a Objetos - Aula 41
Agregação - Python Orientado a Objetos - Aula 42
Composição - Python Orientado a Objetos - Aula 43
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


# agregação
# relação todo-parte fraca onde partes sobrevivem sozinhas
class Filme:
    def __init__(self, nome):
        self.nome = nome


class Favorito:
    def __init__(self):
        self.__filme = []

    @property
    def filme(self):
        return self.__filme

    @filme.setter
    def filme(self, valor):
        self.__filme = valor

    def inserir_filme(self, filme):
        self.filme.extend(filme)

    def listar_filme(self):
        print(f'Filmes:')
        for lista in self.filme:
            print(f'  {lista.nome}')

    def contador(self):
        return f'Adicionado: {len([f for f in self.filme])} filmes'


# extra agregação (estudo a parte)
# relação todo-parte fraca onde partes sobrevivem sozinhas
class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []  # agregação de funcionario


class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []  # agregação de departamentos


# composição
# Endereços de Clientes
class Cliente:
    '''Cliente'''

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._enderecos = []

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @property
    def enderecos(self):
        return self._enderecos.copy()

    def inserir_endereco(self, cidade, *, estado):
        '''Insere Cidade do Cliente'''
        endereco_ = _Endereco(cidade, estado)  # composição
        self._enderecos.append(endereco_)

    def listar_enderecos(self):
        print(f'Cliente: {self.nome}, {self.idade}')
        for endereco in self.enderecos:
            print(f'  Endereço: {endereco.cidade} - {endereco.estado}')

    # apenas para teste, depois comentar
    def __del__(self):
        print(f'{self.nome} FOI APAGADO!')


class _Endereco:
    '''Endereço do Cliente'''

    def __init__(self, cidade: str, estado: str):
        self._cidade = cidade
        self._estado = estado

    @property
    def cidade(self):
        return self._cidade

    @property
    def estado(self):
        return self._estado

    # apenas para teste, depois comentar
    def __del__(self):
        print(f'{self.cidade} - {self.estado} FOI APAGADO!')


# 1. extra composição (estudo a parte)
# classe que será usada dentro de outra
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f'Motor de {self.potencia}CV ligado.')

    def desligar(self):
        print('Motor desligado.')


# classe que usa composição
class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)  # carro TEM um Motor

    def ligar(self):
        print(f'Ligando o carro {self.modelo}')
        self.motor.ligar()

    def desligar(self):
        print(f'Desligando o carro {self.modelo}')
        self.motor.desligar()


# 2. extra composição (estudo a parte)
# todo-parte forte (partes dependem do todo)
class _ItemPedido:  # uso interno da class (conveção)
    '''Item de pedido - criar apenas via Pedido.add_item()'''

    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    @property
    def nome(self):
        return self.produto.nome  # delegar para o Produto

    @property
    def preco(self):
        return self.produto.preco

    @property
    def preco_total(self):
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self, numero):
        self.numero = numero
        self._itens = []  # composição com (protected + convenção)

    @property
    def itens(self):
        '''Apenas leitura - não pode modificar diretamente'''
        return self._itens.copy()  # retorna uma cópia

    # controle total sem setter ([], {})
    # adiciona apenas um produto
    def add_item(self, produto, quantidade):
        # Validação de negócio > 'privacidade técnica'
        if not isinstance(produto, Produto):
            raise ValueError('Produto inválido')
        if quantidade <= 0:
            raise ValueError('Quantidade deve ser positiva')

        # ItemPedido só existe DENTRO do pedido
        # protected interno
        item = _ItemPedido(produto, quantidade)  # criação interna
        # garante mais de um item do pedido
        self._itens.append(item)

    # adiciona multiplos
    def add_itens(self, produtos, quantidades):
        '''Adiciona múltiplos produtos de uma vez'''
        if len(produtos) != len(quantidades):
            raise ValueError('Produtos e quantidades devem ter o mesmo tamanho')

        # list comprehension

        [
            self.add_item(produto, quantidade)  # chama add_item
            for produto, quantidade in zip(produtos, quantidades)
        ]

    def listar_pedidos(self):
        for item_pedido in self.itens:
            print(
                f'Produto: {item_pedido.produto.nome} - Qtd: {item_pedido.quantidade}'
            )
            print(f'  Valor: {item_pedido.preco}')
            print(f'    Total: {item_pedido.preco_total:.2f}'.replace('.', ','))
