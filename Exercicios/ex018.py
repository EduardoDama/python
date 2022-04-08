import math
angulo = float(input('Digite um ângulo qualquer: '))
angulo1 = math.radians(angulo)
cosseno = math.cos(angulo1)
seno = math.sin(angulo1)
tangente = math.tan(angulo1)
print(f'o angulo foi de {angulo} e o cosseno é {cosseno:.2f}, o seno é {seno:.2f}, e a tangente é  {tangente:.2f}')
