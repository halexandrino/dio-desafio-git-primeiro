
menu = """
======Escolha uma das opções abaixo========
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
===========================================
=> """

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def Deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito realizado no valor: R$ {valor:.2f}\n"
        #print(extrato)

    else:
        print("Operação falhou! O valor informado é inválido.")


    print(saldo)
    return saldo, extrato

def Saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    print("Saldo", saldo)

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente!")
        
    elif excedeu_limite:
        print("Operação falhou! você excedeu o limite de valor sacado!")
        
    elif excedeu_saque:
        print("Operação falhou! Você excedeu o limite de saques diário!")
        
    elif valor > 0:
        saldo -= valor
        extrato = f"Saque realizado no valor: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido!")
            
    return saldo, extrato, numero_saques

def Extrato(extrato, saldo):
    print("\n================ EXTRATO Banco Dio================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return None    

while True:
    
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = Deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = Saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        Extrato(extrato, saldo)
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")