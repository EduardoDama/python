valor = input("Digite qualquer coisa: ")
print("===================================================")
print(f"o tipo primitivo desse valor é (\033[m{type(valor)}\033[m)")
print(f"ele é um numero (\033[31m{valor.isnumeric()}\033[m)")
print(f"se ele é um nuemro e uma letra (\033[32m{valor.isalnum()}\033[m)")
print(f"ele é uma letra (\033[33m{valor.isalpha()}\033[m)")
print(f"ele é um digito (\033[34m{valor.isdigit()}\033[m)")
print(f"ele é um numero decimal (\033[35m{valor.isdecimal()}\033[m)")
print(f"Se ele pode ser escrito na tela (\033[36m{ valor.isprintable()}\033[m)")
print(f"se é um espaço (\033[37m{valor.isspace()}\033[m)")
print(f"se o valor está em maiúsculo (\033[31m{ valor.isupper()}\033[m)")
print(f"se o valor está em minúsculo (\033[35m{valor.islower()}\033[m)")
