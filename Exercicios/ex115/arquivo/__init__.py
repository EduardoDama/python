from ex115.interface import *
import selenium
def verific():
    try:
        open('cadastros.txt')
    except:
        open('cadastros.txt', 'x')


def readFile():
    titulo('PESSOAS CADASTRADAS')
    a = open('cadastros.txt').readlines()
    print(f'{"NOME":<31}{"IDADE":>3}')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<30}{dado[1]:>3} anos')


def modific():
    titulo('NOVO CADASTRO')
    name = input('Qual é seu nome?: ')
    while True:
        try:
            yearOld = int(input('Qual é a sua idade?: '))
        except:
            print('\033[31mERRO: Digite um valor válido!\033[m')
        else:
            adic = open('cadastros.txt', 'a+')
            adic.writelines(f'{name};{yearOld}\n')
            return f'O nome {name} foi adicionado ao final da lista.'