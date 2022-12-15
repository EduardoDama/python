class camera:
    def __init__(self, nome, filmando=False, foto=False):
        self.nome = nome
        self.filmando = filmando
        self.fotografia = foto
    
    def filmar(self):
        if self.filmando == True:
            print('Você já está filmando!')
        else:
            print(f'{self.nome} está fimando')
            self.filmando = True

    def foto(self):
        if self.filmando:
            print('Não pode fotografar e filmar ao mesmo tempo!')
        else:
            print(f'{self.nome} está tirando uma foto')

    def pararFilmar(self):
        if self.filmando is False:
            print('Ela já parou de filmar!')
        
        else:
            print(f'{self.nome} parou de filmar')
            self.filmando = False


cam1 = camera('Canon')
cam2 = camera('Soyn')

cam1.filmar()
cam1.foto()
cam1.pararFilmar()
cam1.pararFilmar()
cam1.foto()
