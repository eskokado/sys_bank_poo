# Sistema Bancário Orientado a Objetos
Este projeto é uma aplicação simples de um sistema bancário desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO). O sistema permite o cadastro de clientes, abertura de contas, realização de depósitos, saques e exibição de extratos.

## Estrutura do Projeto
O projeto está organizado em dois arquivos principais:

- sys_bank_oo.py: Contém as definições das classes e a lógica orientada a objetos.
- sys_bank_main.py: Contém as funções e o menu interativo para operar o sistema bancário.

### Arquivo sys_bank_oo.py
Este arquivo define as seguintes classes:

- Transacao: Classe base para as transações bancárias.

  - Deposito: Classe derivada de Transacao para depósitos.
  - Saque: Classe derivada de Transacao para saques.

- Historico: Classe para manter o histórico das transações de uma conta.

- Conta: Classe para representar uma conta bancária.

  - ContaCorrente: Classe derivada de Conta com atributos adicionais de limite e limite de saques.

- Cliente: Classe para representar um cliente bancário.

  - PessoaFisica: Classe derivada de Cliente para representar um cliente pessoa física.

### Arquivo sys_bank_main.py
Este arquivo contém a lógica de interação com o usuário e utiliza as classes definidas em sys_bank_oo.py. Ele implementa as seguintes funcionalidades:

- Cadastrar Cliente: Registra um novo cliente no sistema.
- Cadastrar Conta: Abre uma nova conta para um cliente existente.
- Depositar: Realiza depósitos em uma conta.
- Sacar: Realiza saques de uma conta, respeitando o saldo, limite e número máximo de saques.
- Exibir Extrato: Exibe o extrato da conta, mostrando todas as transações realizadas.
#### Como Executar
- Certifique-se de que você tem o Python instalado em seu sistema.

- Clone este repositório ou baixe os arquivos sys_bank_oo.py e sys_bank_main.py.

- Navegue até o diretório onde os arquivos estão localizados.

- Execute o arquivo sys_bank_main.py com o comando:

```sh
python sys_bank_main.py
```
- Siga as instruções no menu para interagir com o sistema bancário.

#### Exemplo de Uso
- Cadastrar Cliente

  - Escolha a opção [nu] Novo Usuário no menu.
  - Informe os dados do cliente: nome, data de nascimento, CPF e endereço.

- Cadastrar Conta

  - Escolha a opção [nc] Nova Conta no menu.
  - Informe o CPF do cliente para associar a conta ao cliente cadastrado.

- Depositar

  - Escolha a opção [d] Depositar no menu.
  - Informe o CPF do cliente e o valor do depósito.

- Sacar

  - Escolha a opção [s] Sacar no menu.
  - Informe o CPF do cliente e o valor do saque.

- Exibir Extrato

  - Escolha a opção [e] Extrato no menu.
  - Informe o CPF do cliente para exibir o extrato da conta.

- Sair

  - Escolha a opção [q] Sair para encerrar a aplicação.
