'''
Dataclasses - Python Moderno
'''

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


# substitui classes simples
@dataclass
class Produto:
    '''Substitui classes com apenas dados'''

    nome: str
    preco: float
    estoque: int = 0  # valor padrão


@dataclass
class Cliente:
    nome: str
    email: str
    ativo: bool = True  # valor padrão


# métodos e customização
@dataclass
class Pedido:
    numero: int
    cliente: Cliente
    produtos: List[Produto] = field(default_factory=list)
    data_criacao: datetime = field(default_factory=datetime.now)

    # métodos normais como em classes regulares
    def valor_total(self) -> float:
        return sum(p.preco for p in self.produtos)

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def __str__(self) -> str:
        return f'Pedido: {self.numero} - {self.cliente.nome}'


# validações e imutabilidade
@dataclass(frozen=True)  # imutável (como uma tupla nomeada)
class Endereco:
    rua: str
    cidade: str
    estado: str

    def formatado(self) -> str:
        return f'{self.rua}, {self.cidade} - {self.estado}'


@dataclass
class Usuario:
    nome: str
    idade: int
    endereco: Optional[Endereco] = None

    def __post_init__(self):
        '''Validação após inicialização'''
        if self.idade < 0:
            raise ValueError('Idade não pode ser negativa')

    @property
    def maior_idade(self) -> bool:
        return self.idade >= 18


# Versão tradicional (verbosa)
class ProdutoTradicional:
    def __init__(self, nome, preco, estoque=0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __repr__(self):
        return f'ProdutoTradicional(nome="{self.nome}", preco={self.preco}, estoque={self.estoque})'

    def __eq__(self, outro):
        # verifica o tipo primeiro!
        if not isinstance(outro, ProdutoTradicional):
            return False
        return (
            self.nome == outro.nome
            and self.preco == outro.preco
            and self.estoque == outro.estoque
        )


# Versão dataclass (concisa)
@dataclass
class ProdutoModerno:
    nome: str
    preco: float
    estoque: int = 0


# fonte de estudo: DeepSeek
