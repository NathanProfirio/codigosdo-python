from datetime import datetime
import time

opcao = 0
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
limite_saques = 3


def limpa_terminal():
    print("\n"*50)


while True:
    print("""
========= MENU ========= \n    
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair""")

    opcao =(input("==> "))

    #DEPOSITO
    if opcao == "1":
        deposito = float(input("Qual o valor do deposito R$"))
        limpa_terminal()
        if deposito > 0:
            saldo += deposito
            print("{} \nDeposito no valor de R${:.2f} concluido \n{} ".format("="*40, deposito, "="*40))
            data = datetime.now() 
            extrato += (data.strftime("%d/%m/%y %H:%M \n"))
            extrato += "Deposito: R${:.2f} \n\n".format(deposito)
      
        else:
            print("\n{} \nValor inválido \n{} \n".format("="*50,"="*50))

    #SAQUE
    if opcao == "2":
        if numeros_saques < limite_saques:
            saque = float(input("Qual o valor do saque R$"))
            limpa_terminal()
           
            if saque > limite:
                print("{} \nOperação inválida ".format("="*50))
                print("Seu limite maximo e de R${} por saque \n{}".format(limite,"="*50))
           
            elif saque < 0:
                print("\n{} \nValor inválido \n{} \n".format("="*50,"="*50))
           
            elif saque < saldo :
                saldo -= saque
                numeros_saques += 1
                print("{} \nSaque no valor de R${:.2f} concluido \n{}".format("="*40,saque, "="*40))
                extrato += (data.strftime("%d/%m/%y %H:%M \n"))
                extrato += "Saque: -R${:.2f} \n\n".format(saque)
           
            elif saque > saldo:
                print("{} \nO seu saldo atual e R${:.2f} você não pode fazer um saque maior que seu saldo atual \n{}".format("="*85, saldo, "="*85))
                
        elif limite_saques == numeros_saques:
            limpa_terminal()
            print("{} \nVocê ja atingiu o seu limite de 3 saques diarios \n{}".format("="*50,"="*50))
    
    #EXTRATO    
    if opcao == "3":
        limpa_terminal()
        print("{} EXTRATO {}".format("="*20,"="*20))
        print(extrato)
        print("Saldo: R${:.2f}".format(saldo))
        print("="*49)
    
    #Finalização do atendimento
    if opcao == "4":
        print("Saindo ......")
        time.sleep(2)
        limpa_terminal()
        print("{} \nOperação finalizada com sucesso. \n{}".format("="*50,"="*50))
        break    

