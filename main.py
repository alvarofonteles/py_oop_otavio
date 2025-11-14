'''
Classes - Python Orientado a Objetos - Aula 35.
Métodos de Classes (@classmethod) - Python Orientado a Objetos - Aula 36
Métodos estáticos (@staticmethod) - Python POO - Aula 37
@property - Getters e Setters - Python POO - Aula 38
Atributos de Classe - Python POO - Aula 39
Encapsulamento - Python POO - Aula 40
Associação - Python Orientado a Objetos - Aula 41
Agregação - Python Orientado a Objetos - Aula 42
Composição - Python Orientado a Objetos - Aula 43
'''

from classe import Pessoas
from classmethod import Animais
from staticmethod_ import Carros
from property_ import Produtos
from attribute_ import Casa
from encapsulamento import BaseDeDados, ContaBancaria
from relacionamentos import (
    Escritor,
    Caneta,
    MaquinaDeEscrever,
    Produto,
    Carrinho,
    Filme,
    Favorito,
    Funcionario,
    Departamento,
    Empresa,
    Cliente,
    Carro,
    Pedido,
)


# class
def pessoas():

    # Otávio
    p1 = Pessoas('Otávio', 35)
    p1.comer('Batata Frita')  # Otávio 35, está comendo Batata Frita.
    p1.comer('Hamburger')  # Otávio parou de comer Batata Frita
    # Otávio 35, está comendo Hamburger.
    p1.falar('Python')  # Otávio parou de comer Hamburger
    # Otávio 35, está falando sobre Python
    p1.falar('Pyspark')  # Otávio parou de falar Python
    # Otávio 35, está falando sobre Pyspark
    p1.comer('Maçã')  # Otávio parou de falar Pyspark
    # Otávio 35, está comendo Maçã.

    # Informações
    p1.get_dados()  # Otávio tem 35 anos e está saboerando Maçã

    p1.falar('Databricks')  # Otávio parou de comer Maçã
    # Otávio 35, está falando sobre Databricks

    # Informações
    p1.get_dados()  # Otávio tem 35 anos e está discutindo sobre Databricks

    print(f'{p1.get_nome()} nasceu em {p1.get_ano_nasc()}')  # Otávio nasceu em 1990

    print('')
    # Maria
    p2 = Pessoas('Maria', 25)
    p2.comer('Salada de Fruda')  # Maria 25, está comendo Salada de Fruda.
    p2.comer('Sorvete')  # Maria parou de comer Salada de Fruda
    # Maria 25, está comendo Sorvete.
    p2.falar('Culinária')  # Maria parou de comer Sorvete
    # Maria 25, está falando sobre Culinária

    # Informações
    p2.get_dados()  # Maria tem 25 anos e está discutindo sobre Culinária
    p2.falar('Diversão')  # Maria parou de falar Culinária
    # Maria 25, está falando sobre Diversão

    # Informações
    p2.get_dados()  # Maria tem 25 anos e está discutindo sobre Diversão

    print(f'{p2.get_nome()} nasceu em {p2.get_ano_nasc()}')  # Maria nasceu em 2000


# classmethod_
def animais():
    # Instância da Classe
    a1 = Animais('Pastor', 5)
    print('')
    print(a1)  # <classmethod.Animais object at 0x000001CE494F1700>>
    print(f'Seu Pet {a1.nome} tem {a1.idade} anos')  # Seu Pet Pastor tem 5 anos
    print(f'Ele nasceu em {a1.get_ano_nasc()}')  # Ele nasceu em 2020
    print(a1.andar())  # Pastor está andando

    # Método da Classe
    a2 = Animais.por_ano_nasc('Fila', 2020)
    print('')
    print(a2)  # <classmethod.Animais object at 0x000001CE494F17F0>>
    print(f'Seu Pet {a2.nome} tem {a2.idade} anos')  # Seu Pet Fila tem 5 anos
    print(f'Ele nasceu em {a1.get_ano_nasc()}')  # Ele nasceu em 2020
    print(a2.andar(), '\n')  # Fila está andando


# staticmethod_
def carros():
    c1 = Carros('Ferrari')
    c1.correr()

    c2 = Carros('Celta')

    # gera placa (com instância)
    try:
        print('(com instância)')
        try:
            p1 = c1.gera_placa(numero=2, letra='tA')  # (0-9 - A-Z)
            print(p1)
        except Exception as e:
            print(e)  # Letra deve ser um único caractere A-Z, recebido: [tA]
        finally:
            pass

        try:
            p2 = c2.gera_placa(numero=2, letra='S')  # (0-9 - A-Z)
            print(p2)  # BRA2S57
        except Exception as e:
            print(e)
        finally:
            pass

    except Exception as e:
        print(e)

    # gera placa (com a classe)
    print('(com a classe)')
    try:
        p3 = Carros.gera_placa(numero=14, letra='S')  # (0-9 - A-Z)
        print(p3)
    except Exception as e:
        print(e)  # Número deve ser entre 0-9, recebido: [14]
    finally:
        pass

    try:
        p4 = Carros.gera_placa(numero=4, letra='T')  # (0-9 - A-Z)
        print(p4)  # BRA4T22
    except Exception as e:
        print(e)
    finally:
        pass

    try:
        p5 = Carros.gera_placa(numero=17, letra='jL')  # (0-9 - A-Z)
        print(p5)
    except Exception as e:
        print(e)  # Entre 0-9: [17] e/ou Único caractere A-Z: [jL]
    finally:
        pass


# property_
def produtos():

    # entra na validação [R$, r$], [',', '.'] e ['   ']
    print('')
    camisa = Produtos('CAMISA', 'r$ 69,99')
    valor = camisa.desconto(10)  # 10%
    print(
        f'Produto: {camisa.nome} (off: {valor}%) - Valor: R$ {camisa.preco}\n'
    )  # Produto: Camisa (off: 6.3%) - Valor: R$ 62.99

    sapato = Produtos('Sapato', 169.55)
    valor = sapato.desconto(17)  # 17%
    print(
        f'Produto: {sapato.nome} (off: {valor}%) - Valor: R$ {sapato.preco}\n'
    )  # Produto: Sapato (off: 23.92%) - Valor: R$ 140.73

    # Extra (formato BR R$ 0,00)
    calsa = Produtos('Calsa', 236.35)
    valor = calsa.desconto()  # 0%
    print(
        f'Produto: {calsa.nome} (off: {valor}%) - Valor: {calsa.preco_br}\n'
    )  # Produto: Calsa (off: 0.0%) - Valor: R$ 236,35

    bolsa = Produtos('Bolsa', 91.21)
    print(
        f'Produto: {bolsa.nome} - Valor: {bolsa.preco_br}\n'
    )  # Produto: Bolsa - Valor: R$ 91,21

    relogio = Produtos('Relógio', 398.17)
    print(f'Valor: {relogio.preco_br}', '\n')  # Valor: R$ 398,17


# attribute_
def casas():
    # criar duas instâncias
    casa1 = Casa('Sala', 'Vermelho')
    casa2 = Casa('Quarto', 'Azul')

    # Antes
    print(casa1.__dict__)  #  {'comodo': 'Sala', 'cor': 'Vermelho'}
    print(casa2.__dict__)  # {'comodo': 'Quarto', 'cor': 'Azul'}

    # acessando atributo da classe (compartilhado)
    # python verifica: casa.__dict__ não tem banheiros
    # depois procura em: casa.__dict__ encontra banheiros=4
    print(f'casa1.banheiros: {casa1.banheiros}')  # casa1.banheiros: 4
    print(f'casa2.banheiros: {casa2.banheiros}')  # casa2.banheiros: 4

    # alterar atributo da classe afeta TODAS as instâncias
    Casa.set_banheiros(2)  # Modifica via setter (com validação)
    # Acessa via getter
    print(f'Casa.get_banheiros: {Casa.get_banheiros()}')  #  Casa.get_banheiros: 2

    # acessando após mudança na classe
    # ambas ainda usam atributo da classe
    print(f'casa1.banheiros: {casa1.banheiros}')  # casa1.banheiros: 2
    print(f'casa2.banheiros: {casa2.banheiros}')  # casa2.banheiros: 2

    # alterar atributo da instância afeta apenas aquele objeto
    # casa1.banheiros = 3 cria atributo próprio na instância!
    # casa1.__dict__ vira: {'comodo': 'Sala', 'banheiros': 3}
    casa1.banheiros = 3

    # agora casa1 tem próprio banheiros, casa2 ainda usa da classe
    print(f'casa1.banheiros: {casa1.banheiros}')  # casa1.banheiros: 3 (próprio)
    print(f'casa2.banheiros: {casa2.banheiros}')  # casa2.banheiros: 2 (da classe)

    # a classe mantém seu valor original (via getter)
    print(f'Casa.get_banheiros: {Casa.get_banheiros()}')  #  Casa.get_banheiros: 2

    # atributos normais de instância são independentes
    casa1.cor = 'Rosa'
    print(casa1.cor)  # Rosa (apenas casa1)
    print(casa2.cor)  # Azul (apenas casa2)

    # Depois
    print(casa1.__dict__)  # {'comodo': 'Sala', 'cor': 'Rosa', 'banheiros': 3}
    print(casa2.__dict__, '\n')  # {'comodo': 'Quarto', 'cor': 'Azul'}


# encapsulamento
def base_de_dados():
    # Oracle
    db_1 = BaseDeDados(base='Oracle 1')
    db_2 = BaseDeDados(base='Oracle 2')

    db_1.inserir_dado(key=1, nome='Luíz')
    db_1.inserir_dado(key=2, nome='Otávio')
    db_1.inserir_dado(key=3, nome='Miranda')
    db_1.apagar_dado(key=2)
    db_1.listar_dados()
    # base: Oracle 1, id: 1, nome: Luíz
    # base: Oracle 1, id: 3, nome: Miranda

    db_2.inserir_dado(key=4, nome='Ana')
    db_2.inserir_dado(key=5, nome='Maria')
    db_2.inserir_dado(key=6, nome='Lúcia')
    db_2.listar_dados()
    # base: Oracle 2, id: 4, nome: Ana
    # base: Oracle 2, id: 5, nome: Maria
    # base: Oracle 2, id: 6, nome: Lúcia

    # print(db_1.__dados)  # privado (mangling)

    # apenas para consulta (não se deve fazer, boas praticas)
    print(db_1._BaseDeDados__dados)  #  {'Oracle 1': {1: 'Luíz', 3: 'Miranda'}}
    print(db_2._BaseDeDados__dados)  #  {'Oracle 2': {4: 'Ana', 5: 'Maria', 6: 'Lúcia'}}

    # com getter (@property)
    print(db_1.dados)  # {'Oracle 1': {1: 'Luíz', 3: 'Miranda'}}}
    print(db_2.dados, '\n')  # {'Oracle 2': {4: 'Ana', 5: 'Maria', 6: 'Lúcia'}}

    # Sql Server
    db_3 = BaseDeDados(base='Sql Server 1')

    db_3.inserir_dado(key=1, nome='João')
    db_3.inserir_dado(key=2, nome='Flávio')
    db_3.inserir_dado(key=3, nome='Marcos')
    db_3.apagar_dado(key=2)
    db_3.listar_dados()


# extra encapsulamento (estudo a parte)
def contas_bancarias():
    print('')
    c1 = ContaBancaria('Ana', 1000)
    print(c1.titular)  # Ana

    # print(conta._saldo)  # acessa mas errado

    print(c1.saldo)  # 1000
    c1.depositar(500)
    print(c1.saldo)  # 1500

    # print(conta.__senha)  # atributo privado
    # print(conta.senha)  # atributo privado

    c1.sacar(450)
    print(c1.saldo, '\n')  # 1050

    # Conta Otávio
    c2 = ContaBancaria('Otávio')
    print(c2.titular)  # Otávio
    print(c2.saldo)  # 0

    try:
        c2.sacar(450)
    except Exception as e:
        print(e)  # Saldo insuficiente ou valor inválido
    finally:
        pass

    try:
        c2.depositar(0)
    except Exception as e:
        print(e)  # Valor deve ser positivo
    finally:
        pass

    c2.depositar(500)
    print(c2.saldo)  # 500


# relacionamentos
# associação
def associacao():

    # escritor
    escritor = Escritor('Carlos')

    # caneta
    caneta = Caneta('Bic')

    # máquina de escrever
    maquina = MaquinaDeEscrever('Olivetti')

    # lista de ferramentas [1:N]
    escritor.ferramentas.append(caneta)
    escritor.ferramentas.append(maquina)

    # acessando as ferramentas
    print('lista de ferramentas [1:N]')
    for ferramenta in escritor.ferramentas:
        print(f'O Escritor {escritor.nome}, {ferramenta.escrever()} {ferramenta.marca}')
    # O Escritor Carlos, está escrevendo com a Caneta Bic
    # O Escritor Carlos, está escrevendo com a Máquina de escrever Olivetti

    # apenas para testes/demo (desmonta o encapsulamento)
    print('\nTeste Demostrativo [1:N]')
    ferramentas = [caneta, maquina]  # quick and dirty
    for ferramenta in ferramentas:
        print(f'O Escritor {escritor.nome}, {ferramenta.escrever()} {ferramenta.marca}')
    # O Escritor Carlos, está escrevendo com a Caneta Bic
    # O Escritor Carlos, está escrevendo com a Máquina de escrever Olivetti

    # associação escritor [caneta e maquina] [1:1] sobrescreve
    print('\nferramenta [1:1]')
    escritor.ferramenta = caneta
    print(
        f'O Escritor {escritor.nome}, {escritor.ferramenta.escrever()} {caneta.marca}'
    )  # O Escritor Carlos, está escrevendo com a Caneta Bic

    escritor.ferramenta = maquina
    print(
        f'O Escritor {escritor.nome}, {escritor.ferramenta.escrever()} {maquina.marca}\n'
    )  # O Escritor Carlos, está escrevendo com a Máquina de escrever Olivetti

    # se deletar escrito ainda continua independetes [caneta, maqina]
    del escritor
    print(caneta.marca)  # Bic
    print(maquina.escrever(), '\n')  # está escrevendo com a Máquina de escrever

    # extra associação (estudo a parte)
    # produto existe sem carrinho, carrinho usa produtos
    produto1 = Produto('Notebook', 2000)
    produto2 = Produto('Mouse', 150)

    # forma usando o __str__
    print(produto1)  # Notebook - R$ 2000
    print(produto2)  # Mouse - R$ 150

    # implantção simples
    print(produto1.nome)
    print(produto2.preco)

    carrinho = Carrinho()
    carrinho.produtos.append(produto1)  # associação simples
    carrinho.produtos.append(produto2)

    # forma usando o __str__
    print(carrinho)  # Carrinho com 2 produtos:
    # - Notebook - R$ 2000
    # - Mouse - R$ 150

    # implantção simples
    # acesso direto ao indice
    print(carrinho.produtos[0].nome)
    print(carrinho.produtos[1].nome)

    print(carrinho.produtos[0].preco)
    print(carrinho.produtos[1].preco)

    # acesso por loop
    for produtos in carrinho.produtos:
        print(produtos.nome, produtos.preco)


# agregação [1:N]
# relação todo-parte fraca onde partes sobrevivem sozinhas
def agregacao():
    # agregação
    # filme
    f1 = Filme('A Máquina do Tempo')
    f2 = Filme('007 - Missão Impossível')
    f3 = Filme('Caça Fantasmas')
    f4 = Filme('Homem Aranha')

    # lista filmes
    filmes = [f1, f2, f3, f4]

    # favorito
    favorito = Favorito()

    # insere filme favorito
    favorito.inserir_filme(filmes)

    # lista filmes favoritados
    print('')
    favorito.listar_filme()
    # Filmes:
    #   A Máquina do Tempo
    #   007 - Missão Impossível
    #   Caça Fantasmas
    #   Homem Aranha
    # Adicionado: 4 filmes

    # quantidade de filmes favoritados
    print(favorito.contador())
    # Adicionado: 4 filmes

    # extra agregação (estudo a parte)
    # funcionário existe sem departamento
    # TI
    func1 = Funcionario('João', 'Analista')
    func2 = Funcionario('Fábio', 'Dev')
    func3 = Funcionario('Marciel', 'PMO')
    # RH
    func4 = Funcionario('Marta', 'DHO')
    # FI
    func5 = Funcionario('Maria', 'Financeiro')
    func6 = Funcionario('Cláudia', 'Financeiro')

    # departamentos
    depto1 = Departamento('TI')
    depto2 = Departamento('FI')
    depto3 = Departamento('RH')

    # agregação em múltiplos níveis
    # departamento tem funcionários
    # TI
    depto1.funcionarios.extend([func1, func2, func3])
    # RH
    depto3.funcionarios.extend([func4])
    # FI
    depto2.funcionarios.extend([func5, func6])

    # lista de departamento
    departamentos = [depto1, depto2, depto3]

    empresa = Empresa('Nubank')
    empresa.departamentos.extend(departamentos)

    empresas = [empresa]

    # listar funcionario/departamento/empresa
    for emp in empresas:
        print(f'\nEmpresa: {emp.nome}')
        for depto in emp.departamentos:
            print(f'  Departamento: {depto.nome}')
            print(f'    Funcionários:')
            for func in depto.funcionarios:
                print(f'      {func.nome} - {func.cargo}')

    ### Empresa: Nubank
    #   Departamento: TI
    #     Funcionários:
    #       João - Analista
    #       Fábio - Dev
    #       Marciel - PMO
    #   Departamento: FI
    #     Funcionários:
    #       Maria - Financeiro
    #       Cláudia - Financeiro
    #   Departamento: RH
    #     Funcionários:
    #       Marta - DHO


# composição
def composicao():

    #
    # 1. extra composição (estudo a parte)
    print('')
    carro = Carro('Sedan', 120)
    carro.ligar()
    carro.desligar()
    # Ligando o carro Sedan
    # Motor de 120CV ligado.
    # Desligando o carro Sedan
    # Motor desligado.

    '''
    reutilizar código sem criar hierarquias complexas, facilitar manutenção e testes, 
    substituir partes internas sem alterar a interface externa
    '''

    # 2. extra composição (estudo a parte)
    # ItemPedido não existe sem Pedido

    # adiciona apenas um produto
    p1 = Produto('iPhone', 8990.09)
    p2 = Produto('iPed', 3970.5)

    item_pedido = Pedido(965274)
    item_pedido.add_item(p1, 1)  # 1 iPhone
    item_pedido.add_item(p2, 2)  # 2 iPeds

    # adiciona apenas um produto
    print('')
    item_pedido.listar_pedidos()
    # Produto: iPhone - Qtd: 1
    #   Valor: 8990.09
    #     Total: 8990,09
    # Produto: iPed - Qtd: 2
    #   Valor: 3970.5
    #     Total: 7941,00

    # adiciona multiplos
    p1 = Produto('iPhone', 8990.09)
    p2 = Produto('iPed', 3970.5)
    p3 = Produto('MacBook', 17590)

    produtos = [p1, p2, p3]
    quantidades = [1, 2, 2]  # 1 iPhone, 2 iPeds, 2 MacBook

    item_pedido = Pedido(472569)
    item_pedido.add_itens(produtos, quantidades)  # todos de uma vez

    # adiciona multiplos
    print('')
    item_pedido.listar_pedidos()
    # Produto: iPhone - Qtd: 1
    #   Valor: 8990.09
    #     Total: 8990,09
    # Produto: iPed - Qtd: 2
    #   Valor: 3970.5
    #     Total: 7941,00
    # Produto: MacBook - Qtd: 2
    #   Valor: 17590
    #     Total: 35180,00

    #
    # Endereços de Clientes
    print('######## INICIO DA COMPOSIÇÃO ENDEREÇOS DE CLIENTE ########\n')

    c1 = Cliente(nome='Carlinhos', idade=27)
    c2 = Cliente(nome='Marlene', idade=31)
    c3 = Cliente(nome='José', idade=42)

    c1.inserir_endereco('Rio de Janeiro', estado='RJ')
    c1.inserir_endereco('São Paulo', estado='SP')
    c1.inserir_endereco('Curitiba', estado='PR')

    c1.listar_enderecos()
    # Cliente: Carlinhos, 27
    #   Endereço: Rio de Janeiro - RJ
    #   Endereço: São Paulo - SP
    #   Endereço: Curitiba - PR

    # apenas para teste, depois comentar [cliente 1]
    print()
    del c1
    # Carlinhos FOI APAGADO!
    # Curitiba - PR FOI APAGADO!
    # São Paulo - SP FOI APAGADO!
    # Rio de Janeiro - RJ FOI APAGADO!
    # print()

    c2.inserir_endereco('Brasília', estado='DF')
    c2.inserir_endereco('Recife', estado='PE')

    c2.listar_enderecos()
    # Cliente: Marlene, 31
    #   Endereço: Brasília - DF
    #   Endereço: Recife - PE

    c3.listar_enderecos()
    # Cliente: José, 42
    print('\n######## FIM DA COMPOSIÇÃO ENDEREÇOS DE CLIENTE ########')
    # GARABAGE COLLECTION EM ACÃO

    # Marlene FOI APAGADO!
    # Recife - PE FOI APAGADO!
    # Brasília - DF FOI APAGADO!
    # José FOI APAGADO!


# Testes Individuais!
if __name__ == '__main__':
    # class
    pessoas()

    # classmethod_
    animais()

    # staticmethod_
    carros()

    # property_
    produtos()

    # attribute_
    casas()

    # encapsulamento
    base_de_dados()
    contas_bancarias()  # extra

    # relacionamentos
    associacao()
    agregacao()
    composicao()
