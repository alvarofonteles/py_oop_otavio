'''Atributos de Classe - Python POO - Aula 39'''


class Casa:
    # Atributo da classe (compartilhado por todas as instâncias)
    __banheiros = 4  # encapsulado

    def __init__(self, comodo, cor):
        # Atributos da instância (únicos para cada objeto)
        self.comodo = comodo
        self.cor = cor

    @property
    def comodo(self):
        return self._cor

    @comodo.setter
    def comodo(self, valor):
        self._comodo = valor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

    # método para atributo encapsulado
    @classmethod
    def get_banheiros(cls):
        '''Getter - retorna valor atual'''
        return cls.__banheiros

    @classmethod
    def set_banheiros(cls, valor):
        '''Setter - valida antes de modificar'''
        if valor < 0:
            raise ValueError('Banheiros não pode ser negativo')

        cls.__banheiros = valor

    # getter e setter para acessar o atributo da classe encapsulado
    @property
    def banheiros(self):
        """Property da INSTÂNCIA que acessa atributo de CLASSE"""
        return self.get_banheiros()

    @banheiros.setter
    def banheiros(self, valor):
        """Setter da INSTÂNCIA que modifica CLASSE"""
        self.set_banheiros(valor)
