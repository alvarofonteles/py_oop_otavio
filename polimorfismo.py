'''
Extra Polimorfismo Simples - Mesma Interface, Comportamentos Diferentes
Princípio de Liskov (LSP) - Substituição de Tipos
'''


# estrutura simples, apenas didático  (estudo a parte)
# polimorfismo com herança
class Animal:
    def __init__(self):
        self.nome_class = self.__class__.__name__

    def falar(self):
        pass


class Cachorro(Animal):
    def falar(self):  # polimorfismo
        return 'au au!'


class Gato(Animal):
    def falar(self):
        return 'miau!'


class Pato(Animal):
    def falar(self):
        return 'quack!'


class Leao(Animal):
    def falar(self):
        return 'roar!'


# princípio de liskov
# Função polimórfica - aceita QUALQUER Animal
def fazer_barulho(animal: Animal):
    return animal.falar()
