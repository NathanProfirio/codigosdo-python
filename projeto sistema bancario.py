saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
limite_saques = 3
opcao = 0

while opcao != 4:
    print("""====== MENU ======
        
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair""")

    opcao=(int(input("==> ")))



    if opcao == 1:
        deposito = float(input("Qual o valor do deposito: "))
        if deposito > 0:
            saldo += deposito
            extrato += "Deposito: R${:.2f} \n".format(deposito)
        else:
            print("\n{} \nValor inválido \n{} \n".format("="*50,"="*50))

    if opcao == 2:
        if numeros_saques < limite_saques:
            saque = float(input("Qual o valor do saque: "))
            if saque > limite:
                print("{} \nOperação inválida ".format("="*50))
                print("Seu limite maximo de saque e de R${} por saque \n{}".format(limite,"="*50))
            elif saque < 0:
                print("\n{} \nValor inválido \n{} \n".format("="*50,"="*50))
            elif saque < saldo :
                saldo -= saque
                numeros_saques += 1
                extrato += "Saque: -R${:.2f} \n".format(saque)
            elif saque > saldo:
                print("O seu saldo atual e R${:.2f} você não pode fazer um saque maior que seu saldo atual".format(saldo))
                
        elif limite_saques == numeros_saques:
            print("Você ja atingiu o seu limite de 3 saques diarios")
        
    if opcao == 3:
        print("{} EXTRATO {}".format("="*20,"="*20))
        print(extrato)
        print("Saldo: R${:.2f}".format(saldo))
        print("="*49)
        print("\n")



