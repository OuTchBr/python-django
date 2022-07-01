class Conta:
    def __init__(self, nom, sal):
        self.nome = nom
        self.saldo = sal

    def __str__(self):
        return f'Nome: {self.nome} | Saldo: R${self.saldo: .2f}'

    def depositar(self, valor):
        print(f'Anterior:{self}')
        print(f'Depósito:{valor}')
        self.saldo += valor
        print(f'Atual:{self}')

    def sacar(self, valor):
        print('Anterior: ', self)
        print(f'Saque:{valor}')
        self.saldo -= valor
        print('Atual:', self)

    def transferir(self, conta, valor):
        self.sacar(valor)
        conta.depositar(valor)


conta = Conta("Saulo", 100)
conta2 = Conta("Maria", 200)

conta.transferir(conta2, 200)
