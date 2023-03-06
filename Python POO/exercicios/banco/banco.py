class banco:
    def __init__(self):
        self._agencias = sorted([159357, 258456, 268431, 416896])
        self._clientes = sorted(['Eduardo', 'Galinzé', 'Chupas', 'Coranto'])
        self._numero = sorted([2165456, 6561651, 7564656, 1191662])
        self.agencias = []
        self.numero = []
        self.nomesClientes = []

    def Verificar_agencia(self, v):
        if self.agencias[v] in self._agencias:
            return True
        else:
            return False
        
    def Verificar_numero(self, v):
        if self.numero[v] in self._numero:
            return True
        else:
            return False
    
    def Verificar_cliente(self, v):
        if self.nomesClientes[v] in self._clientes:
            return True
        else:
            return False
        

    def autenticar(self, v):
        return self.Verificar_agencia(v) and self.Verificar_cliente(v) and self.Verificar_numero(v)
        
    def depositar(self):
        self.cliente.conta.depositar()