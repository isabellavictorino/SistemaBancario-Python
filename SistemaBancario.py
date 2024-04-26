menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[z] - SAIR

"""

saldo = 0
no_saques = 0
extrato = ""
LIMITE_SAQUES = 3
limite = 500

while True:
    op = input(menu)

    match(op): 
        case "d":
            vl = float(input("Informe o valor do depósito: "))
            if vl > 0:
                saldo += vl
                extrato = f"Depósito de R$ {vl:.2f}. Saldo: {saldo:.2f}\n"
            else:
                print("Valor para depósito inválido")
        
        case "s":
            vl = float(input("Informe o valor do saque: "))
            if vl > saldo:
                print("Operação falhou! Valor de saque maior que o saldo da conta")
            elif no_saques > LIMITE_SAQUES:
                print("Número de saques excedido")
            elif vl > limite:
                print("Valor de saque maior que o limite")
            elif vl > 0:
                saldo -= vl
                extrato = f"Saque de R${vl:.2f}. Saldo: {saldo:.2f}\n"
                no_saques += 1
            else:
                print("O valor informado é inválido")

        case "e":
            print("_________________EXTRATO_________________")
            print("Não foram realizadas movimentações" if not extrato else extrato)
            print(f"\nSaldo: R& {saldo:.2f}")
            print("_________________________________________")
        
        case "z":
            break

        case default:
            print("Opção Inválida")