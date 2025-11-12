'''Métodos estáticos (@staticmethod) - Python POO - Aula 37'''

from random import randint


class Carros:
    def __init__(self, nome):
        self.nome = nome

    def correr(self):
        print(f'{self.nome} está correndo.')

    @staticmethod
    def gera_placa(numero: int, letra: str) -> str:
        '''
        Método Estático
        Cria Placa de Carro a partir de Argumentos e Randint

        Args:
            numero (int): Um número para geração da placa (0-9)
            letra (str): Uma letra para geração da placa (A-Z)

        Returns:
            placa: Placa já criada
        '''
        if not (0 <= numero <= 9) and (len(letra) != 1 or not letra.isalpha()):
            raise ValueError(
                f'Entre 0-9: [{numero}] ' f'e/ou Único caractere A-Z: [{letra}]'
            )

        if not (0 <= numero <= 9):
            raise ValueError(f'Número deve ser entre 0-9, recebido: [{numero}]')

        if len(letra) != 1 or not letra.isalpha():
            raise ValueError(
                f'Letra deve ser um único caractere A-Z, recebido: [{letra}]'
            )

        return (
            f'BRA{numero}{letra.upper()}{randint(10, 99)}'  # BRA2E19 (sempre 2 dígitos)
        )
