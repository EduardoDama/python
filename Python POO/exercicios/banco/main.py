from contas import *
from clientes import *
from banco import *


conta1 = contaCorrente(2165456, 159357, 1000)
cl1 = Cliente('Eduardo', 15)
cl1.conta = conta1

conta2 = contaCorrente(6561651, 258456, 1000)
cl2 = Cliente('Chupas', 69)
cl1.conta = conta2

conta3 = contaCorrente(7564656, 268431, 1000)
cl3 = Cliente('Galinzé', 2)
cl1.conta = conta3

conta4 = contaCorrente(1191662, 416896, 1000)
cl4 = Cliente('Coranto', 15)
cl1.conta = conta4

b = banco()

b.agencias = [conta1.agen, conta2.agen, conta3.agen, conta4.agen]
b.numero = [conta1.num, conta2.num, conta3.num, conta4.num]
b.nomesClientes = [cl1.nome, cl2.nome, cl3.nome, cl4.nome]

if b.autenticar(0):
    conta1.sacar(120, 1)
    conta1.sacar(5, 1)
    conta1.depositar(2235, 1)

if b.autenticar(1):
    conta2.depositar(1235, 2)

if b.autenticar(2):
    conta3.sacar(154, 3)

if b.autenticar(3):
    conta4.depositar(698, 4)




