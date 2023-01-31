from abc import abstractmethod, ABC 

class notificação(ABC):
    def __init__(self, noti):
        self.notificação = noti

    @abstractmethod
    def enviar(self): ...


class notificaçãoEmail(notificação):
    def enviar(self) -> bool: 
        print(f'Email: Enviando "{self.notificação}"')
        return True


class notificaçãoSMS(notificação):
    def enviar(self) -> bool: 
        print(f'SMS: Enviando "{self.notificação}"')
        return False


def notificar(notificaçao: notificação):
    enviando = notificaçao.enviar()

    if enviando:
        print('enviado')
    else:
        print('Não enviado')


notificar(notificaçãoEmail('Obrigado'))
notificar(notificaçãoSMS('UIIII, Cavalo'))