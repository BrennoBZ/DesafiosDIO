def tela_menu():
    menu = """

    ********** MENU **********

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    ==========================

    => """
    return input(menu)

def depositado(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacado(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saques_excedido = numero_saques >= LIMITE_SAQUES

    if saldo_excedido:
        print("A operação é falha! Você não tem saldo suficiente.")
    elif  limite_excedido:
        print("A operação é falha! O valor do saque excede o limite.")
    elif saques_excedido:
        print("A operação é falha! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("A operação é falha! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def extratado(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não se teve movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = tela_menu()

        if opcao == "d":
            saldo, extrato = depositado(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacado(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "e":
            extratado(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()