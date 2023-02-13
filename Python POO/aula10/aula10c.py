class callMe:
    def __init__(self, numero):
        self.num = numero

    def __call__(self, name):
        print(f'Ligando para {self.num}| Nome: {name}')
        

call1 = callMe(1334651)
call1('Eduardo')