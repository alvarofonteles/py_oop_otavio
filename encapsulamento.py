'''Encapsulamento - Python POO - Aula 40'''


class BaseDeDados:
    '''Base de Clientes'''

    def __init__(self, base):
        self._base = base  # protegido (convenção)
        self.__dados = {}  # privado (name mangling)

    @property
    def dados(self):
        return self.__dados

    def inserir_dado(self, key, nome):
        self.__dados.setdefault(self._base, {}).update({key: nome})  # magia setdefault

        # legado
        '''if self._base not in self.dados:
            self.dados[self._base] = {key: nome}  # insere
        else:
            self.dados[self._base].update({key: nome})  # atualiza'''

    def listar_dados(self):
        for base in self.__dados:
            for key, nome in self.__dados[base].items():
                print(f'base: {base}, id: {key}, nome: {nome}')

    def apagar_dado(self, key):
        if not (self._base in self.__dados and key in self.__dados[self._base]):
            raise KeyError(f'Chave {key} não encontrada na base {self._base}')
        
        del self.__dados[self._base][key]


# extra encapsulamento (estudo a parte)
class ContaBancaria:
    '''Conta Bancária (Saldo/Depósito/Saques)'''

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # público
        self._saldo = saldo_inicial  # protegido (convenção)
        self.__senha = '1234A5'  # mangling

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError('Valor deve ser positivo')

        self._saldo += valor

    def sacar(self, valor):
        if not (0 < valor <= self._saldo):
            raise ValueError('Saldo insuficiente ou valor inválido')

        self._saldo -= valor
