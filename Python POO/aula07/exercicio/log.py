class log:
    def log(self, msg):
         raise NotImplementedError('Implemente método log!')

    def erro_log(self, msg):
        return self.log(f'ERRO: {msg}')

    def sucesso_log(self, msg):
        return self.log(f'SUCESSO: {msg}')


class logFileMixin(log):
    def log(self, msg):
        print(msg)

class logPrintMixin(log):
    def log(self, msg):
        print('(LogPrint)')





l = logFileMixin()

l.erro_log('MDS')
