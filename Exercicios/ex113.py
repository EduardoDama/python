
def leiaInt(msg):
    while True:
        try:
            v = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mEscrevo um número inteiro valido!\033[m')
        except (KeyboardInterrupt):
            print('O usuario preferiu não informar esse valor.')
        else:
            return v

def leiaFloat(msg):
    while True:
        try:
            v = float(input(msg))
        except:
            print('\033[31mEscrevo um número real valido!\033[m')
        else:
            return v



n1 = leiaInt('Digite um número inteiro : ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n1} e um número real {n2}')
