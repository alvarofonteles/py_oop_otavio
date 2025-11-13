'''
Classes - Python Orientado a Objetos - Aula 35.
Métodos de Classes (@classmethod) - Python Orientado a Objetos - Aula 36
Métodos estáticos (@staticmethod) - Python POO - Aula 37
@property - Getters e Setters - Python POO - Aula 38
'''

from classe import Pessoas
from classmethod import Animais
from staticmethod_ import Carros
from property_ import Produtos


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
    print(a2.andar())  # Fila está andando


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
    print(f'Valor: {relogio.preco_br}')  # Valor: R$ 398,17


# Testes Individuais!
if __name__ == '__main__':
    pessoas()
    animais()
    carros()
    produtos()
