import textwrap as txw
import os

def menu():
    menu = """
----Bem Vindo ao Santander---
----------- Menu-------------
Digite
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Novo usuário
[5] - Nova Conta
[6] - Listar contas
[0] - Para sair
----------------------
    """
    print(menu) #input(txw.dedent(menu))


def lembrete_saque():
    lembrete_saque = """----------------------------------------
Lembretes:
E permitido realizar 3 saques diarios;
O limite maximo por saque e de R$500,00.
----------------------------------------"""
    return lembrete_saque


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor  
        extrato += f"Depósito:R$ {valor:.2f}\n"
        os.system('cls')
        print("\n---- Depósito realizado com sucesso! ----")
    else:
        print("\n---- Operação falhou! O valor informado e invalido. ----")    
        
    return saldo, extrato
        

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo # valor a sacar maior que o saldo
    excedeu_limite = valor > limite # valor a sacar maior que o limite
    excedeu_saques = numero_saques >= limite_saques # mumero de saques maior que o limite permitido
    
    if excedeu_saldo:
        print("\n---- Operação falhou! Você não tem saldo suficiente. ----")
        
    elif excedeu_limite:
        print("\n---- Operação falhou! O valor do saque excede o valor permitido do limite. ----")
        
    elif excedeu_saques:
        print("\n---- Operação falhou! Número maximo de saques excedido. ----")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n---- Saque realizado com sucesso! ----")
    
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato
    

def exibir_extrato(saldo, /, *, extrato):
    print("\n-------- EXTRATO --------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo:R$ {saldo:.2f}")
    print("---------------------------")


def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (apenas números): ")
    usuario = flitrar_usuario(cpf, usuarios)
   
    if usuario:
       print("\n ---- Usuário ja existe com este CPF! ----")
       
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("---- Usuário criado com sucesso! ----")
     
       
def flitrar_usuario(cpf, usuarios):
    # Cria uma lista vazia para armazenar usuários filtrados
    usuarios_filtrados = []
    
    # Itera sobre cada usuário na lista de usuários
    for usuario in usuarios:
        # Verifica se o CPF do usuário corresponde ao CPF procurado
        if usuario["cpf"] == cpf:
            # Adiciona o usuário à lista de usuários filtrados
            usuarios_filtrados.append(usuario)
    
    # Verifica se a lista de usuários filtrados não está vazia
    if usuarios_filtrados:
        # Retorna o primeiro usuário da lista filtrada
        return usuarios_filtrados[0]
    else:
        # Retorna None se não houver nenhum usuário com o CPF fornecido
        return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = flitrar_usuario(cpf,usuarios)
    
    if usuario:
        print("\n---- Conta criada com sucesso! ----")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n---- Usuário não encontrado, fluxo de criação de conta encerrado! ----")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(txw.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        menu()
        opcao = int(input("Digite a opção desejada: "))
        os.system('cls')
        if opcao == 1: # depositar
            valor = float(input("Digite a quantia que deseja depositar: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)
                
        elif opcao == 2: # sacar
            print(lembrete_saque())
            valor = float(input("Digite o valor que deseja sacar: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
                  
        elif opcao == 3: # extrato
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 4: #criar usuario
            criar_usuario(usuarios)
            
        elif opcao == 5: # criar contas
            # numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 6: # listar contas
            listar_contas(contas)
            
        elif opcao == 0:
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
