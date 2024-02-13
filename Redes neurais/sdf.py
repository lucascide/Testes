class Conta(object):
    def __init__(self, proprietario, numero):
        self.proprietario = proprietario
        self.numero = numero


c = Conta("Lucas", 1234)
print(c.numero)