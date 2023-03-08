from collections import namedtuple
from typing import NamedTuple

class carta(NamedTuple):
    valor: int
    naipe: str = 'NAIPE'

#carta = namedtuple('carta', ['valor', 'naipe'], defaults=['Padrão', 'padrão'])

c1 = carta(5, 'espadas')
print(c1)