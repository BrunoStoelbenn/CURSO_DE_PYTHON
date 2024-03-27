from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    @property
    def get_nome(self):
        return self._nome

    def ligar(self):
        if not self._ligado:
            print(f"Ligando Smartphone {self._nome}...")
            self._ligado = True
        else:
            print(f"O Smartphone {self._nome} já está ligado! ")

    def desligar(self):
        if self._ligado:
            print(f"Desligando Smartphone {self._nome}...")
            self._ligado = False
        else:
            print(f"O Smartphone {self._nome} já está desligado! ")

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)
