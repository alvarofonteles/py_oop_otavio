'''
Conseitos básicos - `@abstractmethod` & `@classmethod` (Completo)
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def falar(self):  # obrigatório para filhos
        pass

    @classmethod
    def criar_com_nome(cls, nome):  # construtor alternativo
        animal = cls()
        animal.nome = nome
        return animal


class Cachorro(Animal):
    def falar(self):  # obrigatório (abstractmethod)
        return "Au au!"
