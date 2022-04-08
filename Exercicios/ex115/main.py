from interface import *
from arquivo import *
from time import sleep
verific()
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar uma pessoa nova', 'Sair do programa'])
    if resp == 1:
        readFile()
    elif resp == 2:
        print(modific())
    elif resp == 3:
        break
    else:
        print(vermelho('ERRO: digite uma opção valida!'))
    sleep(2)
titulo('Saindo do sistema... Até logo!')



