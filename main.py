'''
Classes - Python Orientado a Objetos - Aula 35.
Métodos de Classes (@classmethod) - Python Orientado a Objetos - Aula 36
'''

from classe import Pessoas, Carros
from classmethod import Animais


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


# Implementação para teste '__name__'
def carros():
    c1 = Carros('Ferrari')
    c1.correr()


# Testes Individuais!
if __name__ == '__main__':
    pessoas()
    animais()
    # carros()
