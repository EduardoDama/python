class meuError(Exception): ...

class outroError(Exception): ...

def isso():
    errors =  meuError('Minha primeira classe de Error')
    errors.add_note('Olha a nota 1')
    raise errors

try:
    isso()
except meuError as error:
    print(error)
    raise outroError from error
