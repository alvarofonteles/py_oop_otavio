from classmethod_ import Cachorro
from polimorfismo import (
    Cachorro as Dog,
    Gato,
    Pato,
    Vaca,
    fazer_barulho,
    apresentar_zoologico,
    testar_substituicao,
)
from dataclass_1 import (
    Produto,
    Cliente,
    Pedido,
    Endereco,
    Usuario,
    ProdutoTradicional,
    ProdutoModerno,
)
from dataclass_2 import Cliente as Cli, Vendedor, Produto as Prod, Pedido as Ped


def classmethod_():
    print()
    print('Classmethod')
    rex = Cachorro.criar_com_nome('Rex')  # classmethod
    # abstractmethod implementado
    print(rex.falar())  # 'Au au!'


def polimorfismo():
    '''Demonstração completa do polimorfismo'''

    print()
    print('polimorfismo')
    # Criando diferentes animais
    rex = Dog('Rex')  # alias Cachorro
    felix = Gato('Felix')
    donald = Pato('Donald')
    mimosa = Vaca('Mimosa')

    # Lista polimórfica - todos são Animals!
    zoologico = [rex, felix, donald, mimosa]

    # Polimorfismo básico
    print()
    for animal in zoologico:
        print(fazer_barulho(animal))

    # Rex diz: Au au!
    # Felix diz: Miau!
    # Donald diz: Quack!
    # Mimosa diz: Muuu!

    # Apresentação completa
    print()
    apresentar_zoologico(zoologico)

    # Cachorro: Rex
    #   Rex diz: Au au!
    #   Rex está Correndo atrás do rabo

    # Gato: Felix
    #   Felix diz: Miau!
    #   Felix está Escalando a cortina

    # Pato: Donald
    #   Donald diz: Quack!
    #   Donald está Nadando no lago

    # Vaca: Mimosa
    #   Mimosa diz: Muuu!
    #   Mimosa está Pastando no campo

    # Teste do princípio de Liskov
    print()
    for animal in zoologico:
        teste = testar_substituicao(animal)
        print(f'{animal.nome} pode substituir Animal: {teste}')

    # Rex pode substituir Animal: True
    # Felix pode substituir Animal: True
    # Donald pode substituir Animal: True
    # Mimosa pode substituir Animal: True

    # Posso adicionar QUALQUER novo Animal sem modificar o código existente!
    # Exemplo: class Cobra(Animal), class Papagaio(Animal), etc...


# dataclass_1
def demonstrar_dataclasses():

    print()
    print('dataclass_1')
    print('Dataclasses em Ação')

    # 1. Criação simples
    produto1 = Produto('Notebook', 2500.00, 10)
    produto2 = Produto('Mouse', 89.90)

    print('Produtos (criação automática):')
    print(produto1)  # Produto(nome='Notebook', preco=2500.0, estoque=10)
    print(produto2)  # Produto(nome='Mouse', preco=89.9, estoque=0)
    print()

    # 2. Cliente com valor padrão
    cliente = Cliente('João Silva', 'joao@email.com')
    print('Cliente (valores padrão):')
    print(cliente)  # Cliente(nome='João Silva', email='joao@email.com', ativo=True)
    print(f'Ativo: {cliente.ativo}')  # Ativo: True
    print()

    # 3. Pedido com métodos
    pedido = Pedido(123, cliente, [produto1, produto2])
    print('Pedido (métodos customizados):')
    print(pedido)  # Pedido: 123 - João Silva
    print(f'Valor total: R$ {pedido.valor_total():.2f}')  # Valor total: R$ 2589.90
    print(f'Data: {pedido.data_criacao.strftime('%d/%m/%Y')}')  # Data: 17/11/2025
    print()

    # 4. Endereço imutável
    endereco = Endereco('Rua A, 123', 'São Paulo', 'SP')
    print('Endereco (imutável):')
    print(endereco.formatado())  # Rua A, 123, São Paulo - SP
    # endereco.cidade = 'Rio'  # Erro! frozen=True
    print()

    # 5. Usuario com validação
    usuario = Usuario('Maria', 25, endereco)
    print('Usuario (validação + property):')
    print(f'Nome: {usuario.nome}')  # Nome: Maria
    print(f'Maior idade: {usuario.maior_idade}')  # Maior idade: True
    print(
        f'Endereço: {usuario.endereco.formatado() if usuario.endereco else 'Não informado'}'
    )  # Endereço: Rua A, 123, São Paulo - SP
    print()

    # 6. Comparação automática
    produto3 = Produto('Notebook', 2500.00, 10)
    print('Comparação automática:')
    print(f'produto1 == produto3: {produto1 == produto3}')  # True
    print(f'produto1 == produto2: {produto1 == produto2}')  # False


# dataclass_1
def tradicional_x_dataclass():

    # Mostra a diferença entre abordagens
    print()
    print('dataclass_1')
    print('Comparação: Tradicional x Dataclass')

    tradicional = ProdutoTradicional('Tablet', 1200.00, 5)
    moderno = ProdutoModerno('Tablet', 1200.00, 5)

    print('Tradicional (13 linhas):')
    print(tradicional)  # ProdutoTradicional(nome="Tablet", preco=1200.0, estoque=5)
    print()
    print('Dataclass (4 linhas):')
    print(moderno)  # ProdutoModerno(nome='Tablet', preco=1200.0, estoque=5)
    print()
    print('Mesmo resultado:')
    print(f'trad == moderno: {tradicional == moderno}')  # False
    print(f'moderno == trad: {moderno == tradicional}')  # False
    print(f'moderno == moderno: {moderno == moderno}')  # True
    print(f'trad is moderno: {tradicional is moderno}')  # False


def dataclass_1():
    demonstrar_dataclasses()
    tradicional_x_dataclass()


def dataclass_2():
    '''Demonstra todos os conceitos juntos'''

    # 1. Criação dos objetos
    cliente = Cli('João Silva', 30, '11-99999-8888', vip=True)
    vendedor = Vendedor('Maria Santos', 28, 0.15)

    produto1 = Prod('Notebook', 2500.00, 'Eletrônicos')
    produto2 = Prod('Mouse', 89.90, 'Acessórios')
    produto3 = Prod('Teclado', 150.00, 'Acessórios')

    # 2. Composição - Pedido com múltiplas relações
    pedido = Ped(123, cliente, vendedor)
    pedido.adicionar_item(produto1, 1)
    pedido.adicionar_item(produto2, 2)
    pedido.adicionar_item(produto3, 1)

    print()
    print('dataclass_2')
    print('Composição - Pedido com múltiplas relações:')
    print(pedido)  # Pedido #123 - João Silva
    print(
        f'Cliente: {pedido.cliente.nome} (VIP: {pedido.cliente.vip})'
    )  #  Cliente: João Silva (VIP: True)
    print(f'Vendedor: {pedido.vendedor.nome}')  # Vendedor: Maria Santos
    print(f'Total: R$ {pedido.total:.2f}')  # Total: R$ 2829.80
    print(
        f'Com desconto VIP: R$ {pedido.total_com_desconto:.2f}'
    )  # Com desconto VIP: R$ 2405.33
    print(
        f'Comissão vendedor: R$ {pedido.comissao_vendedor():.2f}'
    )  # Comissão vendedor: R$ 424.47

    # 3. Detalhes dos itens (composição aninhada)
    print()
    print('Composição Aninhada - Itens do pedido:')
    for i, item in enumerate(pedido.itens, 1):
        print(f'{i}. {item.produto.nome} - {item.quantidade}x')
        print(f'  Subtotal: R$ {item.subtotal:.2f}')

    # 1. Notebook - 1x
    #   Subtotal: R$ 2500.00
    # 2. Mouse - 2x
    #   Subtotal: R$ 179.80
    # 3. Teclado - 1x
    #   Subtotal: R$ 150.00

    # 4. Polimorfismo
    print()
    print('Polimorfismo')
    pessoas = [cliente, vendedor]
    for pessoa in pessoas:
        print(
            f"{pessoa.nome} ({pessoa.__class__.__name__}): {pessoa.atividade_principal()}"
        )
    # João Silva (Cliente): Fazendo compras
    # Maria Santos (Vendedor): Vendendo produtos

    # 5. Herança e propriedades
    print()
    print('Herança - Propriedades da classe base:')
    for pessoa in pessoas:
        print(f'{pessoa.nome}:')
        print(f'  Idade: {pessoa.idade}')
        print(f'  Maior idade: {pessoa.maior_idade}')
        print(f'  Tipo: {pessoa.__class__.__name__}')

    # João Silva:
    #   Idade: 30
    #   Maior idade: True
    #   Tipo: Cliente
    # Maria Santos:
    #   Idade: 28
    #   Maior idade: True
    #   Tipo: Vendedor


# Testes Individuais!
if __name__ == '__main__':
    classmethod_()
    polimorfismo()
    dataclass_1()
    dataclass_2()

# fonte de estudo: DeepSeek
