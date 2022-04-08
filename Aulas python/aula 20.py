def dobra(valor):
   pos = 0
   while pos < len(valor):
      valor[pos] *= 2
      pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores) 
