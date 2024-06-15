from datetime import date
from typing import List

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero: int, agencia: str = "0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def nova_conta(self, cliente, numero:int):
        return Conta(cliente, numero)
    
    def sacar(self, valor: float) -> bool:
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(Saque(valor))
            return True
        return False
    
    def depositar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        return False
    
class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class ContaCorrente(Conta):
    def __init__(self, cliente, numero: int, agencia: str, limite: float, limite_saques: int):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques