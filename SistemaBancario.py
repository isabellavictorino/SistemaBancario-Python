import textwrap

#menu
def menu():
    menu = """
    ______________MENU______________
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova Conta
    [l]\tListar Conta
    [u]\tNovo Usuário
    [z]\tSair
    -> """
    return input(textwrap.dedent(menu))

#depósito
def deposito(saldo,extrato,valor):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\t R$ {valor:.2f}\n' #\t - tab
        print('Depósito realizado com sucesso!')
    else:
        print('Operação falhou! O valor é inválido')

    return saldo, extrato

#saque
def sacar(*,saldo,valor,extrato,limite,n_saques,limite_saques):
    if valor > saldo:
        print('Saldo insuficiente')
    elif valor > limite:
        print('Limite insuficiente')
    elif n_saques > limite_saques:
        print('Número máximo de saques excedido')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\tR${valor:.2f}\n'
    else:
        print('Valor inválido')

    return saldo, extrato

#extrato
def mostrar_extrato(saldo,extrato):
    print('\n_______________EXTRATO_______________')
    print('Não foram realizadas movimentações' if not extrato else extrato)
    print(f'\nSaldo:\tR${saldo:.2f}')
    print('_____________________________________')

#criar usuarios
def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('CPF já está em uso')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: ')
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print('Usuário criado com sucesso!')

def filtrar_usuario(cpf,usuarios):
    usuarios_filt = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filt[0] if usuarios_filt else None

def criar_conta(agencia, no_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {"agencia": agencia, "numero_conta": no_conta, "usuario": usuario}
    print('Usuário não encontrado')

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("_" * 100)
        print(textwrap.dedent(linha))

def banco():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 0
    extrato = ''
    n_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            saldo,extrato = deposito(saldo,extrato,valor)
        
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                n_saques=n_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            mostrar_extrato(saldo,extrato)
        
        elif opcao == 'u':
            criar_usuario(usuarios)

        elif opcao == 'n':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta,usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'l':
            listar_contas(contas)

        elif opcao == 'z':
            break

        else:
            print('Operação Inválida')

banco()
