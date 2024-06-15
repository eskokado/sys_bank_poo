from sys_bank_oo import PessoaFisica, ContaCorrente, Deposito, Saque
from datetime import date


usuarios = []
contas = []

def cadastrar_cliente(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Já existe um usuário com esse CPF.")
            return
    
    data_nascimento = date(*map(int, data_nascimento.split("/")[::-1]))
    cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
    usuarios.append(cliente)
    print("Usuário cadastrado com sucesso.")

def cadastrar_conta(cpf):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            numero_conta = len(contas) + 1
            conta = ContaCorrente(usuario, numero_conta, "0001", limite=500.0, limite_saques=3)
            usuario.adicionar_conta(conta)
            contas.append(conta)
            print("Conta cadastrada com sucesso.")
            return
        
    print("Usuário não encontrado")

def contar_saques(conta):
    return sum(1 for transacao in conta.historico.transacoes if isinstance(transacao, Saque))

def sacar(conta: ContaCorrente, valor: float):
    if valor > conta.saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > conta.limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif contar_saques(conta) >= conta.limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        if conta.sacar(valor):
            print(f"Saque de R$ {valor: .2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def depositar(conta: ContaCorrente, valor: float):
    if valor > 0:
        conta.depositar(valor)
        print(f"Depósito de R$ {valor: .2f} realizado com sucesso.")
    else:
        print(f"Operação falhou! O valor informado é inválido.")

def exibir_extrato(conta: ContaCorrente):
    print("\n================ EXTRATO ================")
    if not conta.historico.transacoes:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta.historico.transacoes:
            if isinstance(transacao, Deposito):
                print(f"Depósito: R$ {transacao.valor: .2f}")
            elif isinstance(transacao, Saque):
                print(f"Saque: R$ {transacao.valor: .2f}")
    
    print(f"\nSaldo: R$ {conta.saldo: .2f}")
    print("==========================================")

def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [q] Sair
    
    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            for conta in contas:
                if conta.cliente.cpf == cpf:
                    valor = float(input("Informe o valor do depósito: "))
                    depositar(conta, valor)
                    break
                else:
                    print("Conta não encontrada.")

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            for conta in contas:
                if conta.cliente.cpf == cpf:
                    valor = float(input("Informe o valor do saque: "))
                    sacar(conta, valor)
                    break
            
                else:
                    print("Conta não encontrada.")
    
        elif opcao == 'e':
            cpf = input("Informe o CPF do cliente: ")
            for conta in contas:
                if conta.cliente.cpf == cpf:
                    exibir_extrato(conta)
                    break
                else:
                    print("Conta não encontrada.")

        elif opcao == "nu":
            nome = input("Informe o nome do cliente: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Informe o CPF: ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            cadastrar_cliente(nome, data_nascimento, cpf, endereco)

        elif opcao == "nc":
            cpf = input("Informe o CPF do cliente: ")
            cadastrar_conta(cpf)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()