import re
import sys

def limpa_terminal():
    print("\n"*50)

def linhas():
    print("=" * 60)

linhas()
print("Nesse programa você pode verificar se um cpf e valido ou não")
linhas()
print("\n")

while True:
    cpf_do_usuario = input("Digite o cpf: ")
    cpf_tratado = re.sub(r"[^0-9]","",cpf_do_usuario)
    
    if len(cpf_tratado) != 11:
        linhas()
        print('Número digitado invalido um cpf deve conte 11 digitos')
        linhas()
        print("\n")
        continue

    cpf_formatado = ""
    contador_regressivo = 10
    contador_do_loop = 0
    soma_primeiros_digitos = 0
    soma_segundo_digito = 0


    #Verifica se o usuario digitos so numeros iguais
    if cpf_do_usuario == cpf_do_usuario[0] * len(cpf_do_usuario):
        linhas()
        print("Você digitou um cpf invalido com caracteres repetidos")
        linhas()
        continue

    #calcular o primeiro digito verificado
    for primeiro in cpf_tratado[:9]:
        soma_primeiros_digitos += int(primeiro) * contador_regressivo
        contador_regressivo -= 1
        
    mult_resto_divisao = (soma_primeiros_digitos * 10) % 11

    if mult_resto_divisao > 9:
        primeiro_digito = 0
    else:
        primeiro_digito = mult_resto_divisao

    #Verificar o segundo codigo verificado
    contador_regressivo = 11
    for segundo in cpf_tratado[:10]:
        soma_segundo_digito += int(segundo) * contador_regressivo
        contador_regressivo -= 1
        mult_resto_divisao = (soma_segundo_digito * 10) % 11

    if mult_resto_divisao > 9:
        segundo_digito = 0
    else:
        segundo_digito = mult_resto_divisao

    #Formata o cpf para mostra no final 
    for formatacao in cpf_tratado:
        if contador_do_loop == 2:
            formatacao += "."
            contador_do_loop += 1
        if contador_do_loop == 6:
            formatacao += "."
            contador_do_loop += 1
        if contador_do_loop  == 10:
            formatacao += "-"
            contador_do_loop += 1
        cpf_formatado += formatacao
        contador_do_loop += 1

    #verifica se o cpf digitado e valido ou não 
    if str(primeiro_digito) == cpf_tratado[9] and str(segundo_digito) == cpf_tratado[10]:
        limpa_terminal()
        linhas()
        print(f"O cpf {cpf_formatado} e valido")
        linhas()

        #Verifica se o usuario deseja verificar outro cpf
        while True:
            verificar_novo_cpf = input("Você deseja verificar outro cpf \n[1] SIM \n[2] NÂO \n==> ")
            if verificar_novo_cpf == "1":
                print("\n")
                break
            elif verificar_novo_cpf == "2":
                limpa_terminal()
                linhas()
                print("Obrigado por usar esse validador de CPF")
                print("Criador por Nathan alves profirio")
                print("Encerrando o programa Tenha um ótimo dia!")
                linhas()
                sys.exit()
            else:
                print("Resposta invalida digite 1 para SIM e 2 para NÃo")
    else:
        limpa_terminal()
        linhas()
        print(f"O cpf {cpf_formatado} e invalido")
        linhas()

        #Verifica se o usuario deseja verificar outro cpf
        while True:
            verificar_novo_cpf = input("Você deseja verificar outro cpf \n[1] SIM \n[2] NÂO \n==> ")
            if verificar_novo_cpf == "1":
                break
            elif verificar_novo_cpf == "2":
                limpa_terminal()
                linhas()
                print("Obrigado por usar esse validador de CPF")
                print("Criador por Nathan alves profirio")
                print("Encerrando o programa Tenha um ótimo dia!")
                linhas()
                sys.exit()
            else:
                print("Resposta invalida digite 1 para SIM e 2 para NÃo")