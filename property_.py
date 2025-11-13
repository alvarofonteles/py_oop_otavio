'''@property - Getters e Setters - Python POO - Aula 38'''


class Produtos:
    def __init__(self, nome: str, preco: int | float):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self._nome.title()  # capitalizado

    @nome.setter
    def nome(self, valor):
        if not valor.strip():
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor.strip()

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):

        if isinstance(valor, str):
            # Remove R$ e espaços
            valor = float(valor.upper().replace('R$', '').strip().replace(',', '.'))

        if not isinstance(valor, (int, float)):
            raise ValueError('Somente valor numérico')

        if valor < 0:
            raise ValueError('O Preço não pode ser negativo!')

        # arredonda valor [0.00]
        self._preco = round(valor, 2)  # atribui ao interno

    def desconto(self, percentual: int | float = 0) -> float:
        '''Retorna valor com desconto'''
        if not (0 <= percentual <= 100):
            raise ValueError('Desconto deve ser entre 0% e 100%')

        # lê valor atual (getter)
        # atribui novo valor (setter com validação)
        # getter     setter
        self.preco = self.preco * (1 - percentual / 100)

        return round(self.preco * (percentual / 100), 2)

    # Extra (formato BR R$ 0,00)
    @property
    def preco_br(self) -> str:
        '''Retorna preço formatado como R$ 69,99'''
        return (
            f'R$ {self._preco:,.2f}'.replace(',', 'X')
            .replace('.', ',')
            .replace('X', '.')
        )

    # regra antiga desconto (não deletar)
    def desconto_old(self, percentual):
        self.preco -= self.preco * (percentual / 100)
        self.preco = round(self.preco, 2)
