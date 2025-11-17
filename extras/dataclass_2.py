'''
Dataclasses Avançadas - Herança, Polimorfismo e Composição
'''

from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from dataclasses import dataclass, field


# HERANÇA com Dataclass
@dataclass
class Pessoa(ABC):
    '''Classe base abstrata'''

    nome: str
    idade: int

    @abstractmethod
    def atividade_principal(self) -> str:
        pass

    @property
    def maior_idade(self) -> bool:
        return self.idade >= 18


@dataclass
class Cliente(Pessoa):
    '''Herda de Pessoa + dados específicos'''

    telefone: str
    vip: bool = False

    def atividade_principal(self) -> str:  # Polimorfismo
        return "Fazendo compras"

    def desconto_vip(self) -> float:
        return 0.15 if self.vip else 0.0


@dataclass
class Vendedor(Pessoa):
    '''Outra subclasse com comportamento diferente'''

    comissao: float = 0.1
    ativo: bool = True

    def atividade_principal(self) -> str:  # Polimorfismo
        return "Vendendo produtos"

    def calcular_comissao(self, valor_venda: float) -> float:
        return valor_venda * self.comissao


# COMPOSIÇÃO com Dataclass
@dataclass
class Produto:
    nome: str
    preco: float
    categoria: str


@dataclass
class ItemPedido:
    produto: Produto  # Composição
    quantidade: int = 1

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade


@dataclass
class Pedido:
    numero: int
    cliente: Cliente  # Composição
    vendedor: Vendedor  # Composição
    itens: List[ItemPedido] = field(default_factory=list)
    data: datetime = field(default_factory=datetime.now)

    @property
    def total(self) -> float:
        return sum(item.subtotal for item in self.itens)

    @property
    def total_com_desconto(self) -> float:
        desconto = self.cliente.desconto_vip()
        return self.total * (1 - desconto)

    def comissao_vendedor(self) -> float:
        return self.vendedor.calcular_comissao(self.total)

    def adicionar_item(self, produto: Produto, quantidade: int = 1):
        self.itens.append(ItemPedido(produto, quantidade))

    def __str__(self) -> str:
        return f"Pedido #{self.numero} - {self.cliente.nome}"


# fonte de estudo: DeepSeek
