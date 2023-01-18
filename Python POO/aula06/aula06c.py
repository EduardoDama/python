class cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereço = []
    
    def inserir(self, rua, número):
        self.endereço.append(endereco(rua, número))

    def listar(self):
        print('-='*20)
        for ender in self.endereço:
            print(ender.rua, ender.numero)
        
        print('-='*20)



class endereco:
    def __init__(self, rua, núemro) -> None:
        self.rua = rua
        self.numero = núemro

    def __del__(self):
        print('escluíndo')

cli1 = cliente('Eduardo')
cli1.inserir('Catalunha', 2665)
cli1.inserir('Barcelona', 32165)
cli1.inserir('Brasiçá', 21515)
cli1.listar()

del cli1