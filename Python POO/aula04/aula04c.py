class conection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.senha = None #Método de instância , tem o Self

    def set_user(self, name):
        self.user = name
    
    def set_senha(self, senha):
        self.senha = senha

    @classmethod
    def criar_user_padrao(cls, user, senha):
        cone = cls()
        cone.user = user
        cone.senha = senha

        return cone

p1 = conection()

p1.set_user('Eduardo')
print(p1.user)

p1.set_senha(6115365414215611651451)
print(p1.senha)

p2 = conection.criar_user_padrao('Eduardo', '123456789')
print(p2.user, p2.senha)