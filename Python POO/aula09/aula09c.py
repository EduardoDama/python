class A:
    def __new__(cls, *args, **kwargs):
        print('Estou no NEW, Antes da criação do objeto')
        return super().__new__(cls)
    
    def __init__(self, x):
        self.x = x
        print('Agora estou no INIT, objeto criado')
        print(self)

    def __repr__(self) -> str:
        return 'A()'



a = A(1230)
print(a.x)