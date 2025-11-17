'''
Polimorfismo Avançado - Princípio de Liskov (Substituição de Tipos)
'''

from abc import ABC, abstractmethod
from typing import List


# interface base com ABC (abstract base class)
class Animal(ABC):
    '''Classe abstrata - não pode ser instanciada diretamente'''

    def __init__(self, nome: str):
        self._nome = nome
        self.nome_classe = self.__class__.__name__

    @property
    def nome(self) -> str:
        return self._nome

    @abstractmethod
    def falar(self) -> str:
        '''Método abstrato - deve ser implementado pelas subclasses'''
        pass

    @abstractmethod
    def mover(self) -> str:
        '''Outro método abstrato para demonstrar múltiplos comportamentos'''
        pass

    def __str__(self) -> str:
        return f'{self.nome_classe}: {self.nome}'


# implementações concretas
class Cachorro(Animal):
    def falar(self) -> str:
        return 'Au au!'

    def mover(self) -> str:
        return 'Correndo atrás do rabo'


class Gato(Animal):
    def falar(self) -> str:
        return 'Miau!'

    def mover(self) -> str:
        return 'Escalando a cortina'


class Pato(Animal):
    def falar(self) -> str:
        return 'Quack!'

    def mover(self) -> str:
        return 'Nadando no lago'


class Vaca(Animal):
    def falar(self) -> str:
        return 'Muuu!'

    def mover(self) -> str:
        return 'Pastando no campo'


# funções polimórficas
def fazer_barulho(animal: Animal) -> str:
    '''Aceita QUALQUER Animal - Princípio de Liskov'''
    return f'{animal.nome} diz: {animal.falar()}'


def descrever_movimento(animal: Animal) -> str:
    '''Outra função genérica que funciona com todos os animais'''
    return f'{animal.nome} está {animal.mover()}'


def apresentar_zoologico(animais: List[Animal]) -> None:
    '''Função que demonstra polimorfismo em coleções'''

    # apresentando o zoológico polimórfico!
    for animal in animais:
        print(f'{animal}')
        print(f'  {fazer_barulho(animal)}')
        print(f'  {descrever_movimento(animal)}')
        print()


# teste do princípio de Liskov
def testar_substituicao(animal: Animal) -> bool:
    '''Testa se qualquer subclasse pode substituir Animal'''
    try:
        barulho = animal.falar()
        movimento = animal.mover()
        return bool(barulho and movimento)  # se funcionou, retorna True
    except Exception:
        return False


# fonte de estudo: DeepSeek
