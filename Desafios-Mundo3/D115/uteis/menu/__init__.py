def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError,TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n
        
def linha(tam=42):
    print('-'*tam)

def cabecalho(texto,alinhamento=1):
    linha()
    if alinhamento == 1:
        print(texto)
    elif alinhamento == 2:
        print(f'{texto:>42}')
    elif alinhamento == 3:
        print(f'{texto:^42}')
    linha()

def menu(lista):
    cabecalho('MENU PRINCIPAL',3)
    c = 1
    for item in lista:
        print(f'\033[32m{c} -\033[m \033[36m{item}\033[m')
        c+=1
    linha()
    opc = leiaInt('\033[35mDigite sua opção: \033[m')
    return opc

