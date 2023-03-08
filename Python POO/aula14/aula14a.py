from dataclasses import dataclass, asdict, astuple, field, fields

@dataclass
class Pessoa:
    nome: str = field(default='Eduardo')
    sobrenome: str = field(default_factory=str)
    endereços: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.nomeCompleto = f'{self.nome} {self.sobrenome}'
        


p1 = Pessoa(sobrenome='Damasceno')
print(asdict(p1), astuple(p1))

p1.endereços = ['sdasda', 'sdaas', 'hbdbhfd']

print(fields(p1))