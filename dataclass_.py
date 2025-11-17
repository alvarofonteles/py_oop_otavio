'''Python Dataclasses - pare de criar classes desnecessárias'''

from dataclasses import dataclass, field


class OldPerson:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.class_name = self.__class__.__name__

    def __str__(self):
        class_str = f'({self.class_name}) ({self.name} {self.lastname})'
        return class_str

    def __repr__(self):
        return str(self)  # retorna o __srt__ acima

    def __eq__(self, outro):  # value ou other ou outro é o que será comparado
        return self.lastname == outro.lastname


@dataclass(kw_only=True)
class Person:
    name: str
    lastname: str
    class_name: str = field(init=False)
    active: bool = False
    # adresses: list = [] # ValueError: default_factory
    adresses: list = field(default_factory=list)
    full_name: str = field(default='Missing', init=True)

    def __post_init__(self):
        self.class_name = self.__class__.__name__
        self.full_name = f'{self.name} {self.lastname}'

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.lastname == other.lastname  # Só compara lastname

    def get_full_name(self):
        return self.full_name

    @property
    def prop_full_name(self):
        return self.full_name
