from pathlib import Path

CAMINHO_LOG = Path(__file__).parent / 'log.txt'
class log:
    def log(self, msg):
         raise NotImplementedError('Implemente método log!')

    def erro_log(self, msg):
        return self.log(f'ERRO: {msg}')

    def sucesso_log(self, msg):
        return self.log(f'SUCESSO: {msg}')


class logFileMixin(log):
    def log(self, msg):
        print('salvando...')
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        log = open(CAMINHO_LOG, 'a')
        log.write(msg_formatada)
        log.write('\r\n')

class logPrintMixin(log):
    def log(self, msg):
        print(f'{msg} (LogPrint)')



if __name__ == '__main__':
    l = logFileMixin()
    l.erro_log('Dahora')
    l.sucesso_log('Agora sim')



