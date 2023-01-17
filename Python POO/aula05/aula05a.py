class issoAi:
    def __init__(self):
        self.publico = 'Isso é público!'
        self._protected = 'isso é protegido'
        self.__privet = ' Isso é privao'

    def publico(self):
        return 'Método publico'
    
    def _protegido(self):
        return 'Método protegido'

    def __privado(self):
        return 'Método privado'


f = issoAi()

