import re
import sys

#Função criada para limpar o terminal e deixa o programa mais organizado
def limpa_terminal():
    print("\n"*50)

#Função criada para criar as linhas dos menus e mensagens de erros
def linhas():
    print("=" * 60)

#Função criada para pergunta para o usuário no final do programa se ele dejesa usa novamente o validador de cpf ou que sair do programa
def deseja_continuar():
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

#mostra para o usuário a função do programa
linhas()
print("Nesse programa você pode verificar se um cpf e valido ou não")
linhas()
print("\n")

#Inicio do programa pergunta para o usuário qual o cpf ele que validar e trata alguns erros de digitação depois verifica se o numero digitado tem 11 digitos
while True:
    cpf_do_usuario = input("Digite o cpf: ")
    cpf_tratado = re.sub(r"[^0-9]","",cpf_do_usuario)
    
    if len(cpf_tratado) != 11:
        linhas()
        print('Número digitado invalido um cpf deve conte 11 digitos')
        linhas()
        print("\n")
        continue
    
    #Verifica se o usuário digitos somente numeros iguais
    if cpf_do_usuario == cpf_do_usuario[0] * len(cpf_do_usuario):
        linhas()
        print("Você digitou um cpf invalido somente com caracteres repetidos")
        linhas()
        continue

    #criação das variaveis usadas durante a validação do cpf
    contador_regressivo = 10
    contador_das_repeticoes = 0
    soma_primeiros_digitos = 0
    soma_segundo_digito = 0
    cpf_formatado = ""

    #calcular o primeiro digito verificado
    for primeiro in cpf_tratado[:9]:
        soma_primeiros_digitos += int(primeiro) * contador_regressivo
        contador_regressivo -= 1
        
    mult_resto_divisao = (soma_primeiros_digitos * 10) % 11

    if mult_resto_divisao > 9:
        primeiro_digito = 0
    else:
        primeiro_digito = mult_resto_divisao

    #Calcular o segundo codigo verificado
    contador_regressivo = 11
    for segundo in cpf_tratado[:10]:
        soma_segundo_digito += int(segundo) * contador_regressivo
        contador_regressivo -= 1
        mult_resto_divisao = (soma_segundo_digito * 10) % 11

    if mult_resto_divisao > 9:
        segundo_digito = 0
    else:
        segundo_digito = mult_resto_divisao

    #Formata o numero digitado pelo usuário para o padrão do cpf 000.000.000-00
    for formatacao in cpf_tratado:
        if contador_das_repeticoes == 2:
            formatacao += "."
            contador_das_repeticoes += 1
        if contador_das_repeticoes == 6:
            formatacao += "."
            contador_das_repeticoes += 1
        if contador_das_repeticoes  == 10:
            formatacao += "-"
            contador_das_repeticoes += 1
        cpf_formatado += formatacao
        contador_das_repeticoes += 1

    #verifica e mostra se o cpf digitado e valido ou não 
    if str(primeiro_digito) == cpf_tratado[9] and str(segundo_digito) == cpf_tratado[10]:
        limpa_terminal()
        linhas()
        print(f"O cpf {cpf_formatado} e valido")
        linhas()
        deseja_continuar()

    else:
        limpa_terminal()
        linhas()
        print(f"O cpf {cpf_formatado} e invalido")
        linhas()
        deseja_continuar()
        