'''Aprenda a usar Metaclass no Python e entenda como as classes são criadas'''


class City:
    def __init__(self, name, neighborhood):
        self.name = name
        self.neighborhood = neighborhood

    def __repr__(self):
        return f'Cidade: {self.name} - Bairro: {self.neighborhood}'


def init_neighborhood(self, name, code_postal):
    self.name = name
    self.code_postal = code_postal


# criando class a partir da class type
Neighborhood = type(
    'Neighborhood',  # nome da class
    (),  # class que herdam - tupla()
    {'__init__': init_neighborhood},  # namespace {} # init da class
)


# metaclass
class MetaDog(type):
    def __new__(mcs, name, bases, namespace):
        print('__new__ da metaclass')
        cls = super().__new__(mcs, name, bases, namespace)
        return cls


class Dog(metaclass=MetaDog):
    def __new__(cls, *args, **kwargs):
        print('__new__ da class')
        return super().__new__(cls)

    def __init__(self, name, age):
        print('__init__ da class')
        self.name = name
        self.age = age


# ensino extra
# créditos: Prof. Otávio Miranda
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        namespace['adicionei'] = 'um valor'

        cls = super().__new__(mcs, name, bases, namespace)

        for base in bases:
            for key, value in base.__dict__.items():
                if getattr(value, '__is_abstract__', False):
                    if key not in cls.__dict__.keys():
                        raise NotImplementedError(
                            f'{key} not implemented in {cls.__name__}'
                        )

        return cls


def abstractmethod(method):
    method.__is_abstract__ = (
        True  # if True ->> NotImplementedError: full_name not implemented in Person
    )
    return method


class SuperPerson(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('__new__ da class')
        return super().__new__(cls)

    def __init__(self, name, lastname):
        print('__init__ da class')
        self.name = name
        self.lastname = lastname

    @abstractmethod
    def full_name(self): ...


class Person(SuperPerson):
    @property
    def full_name(self):
        return f'{self.name} {self.lastname}'
