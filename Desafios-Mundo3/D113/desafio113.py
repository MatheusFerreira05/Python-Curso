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
        
def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except(ValueError,TypeError):
            print('\033[31mErro: por favor, digite um número real válido.\033[m')
        except(KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n
        

numero = leiaInt('Digite um valor: ')
numero2 = leiaFloat('Digite um valor: ')
print(f'O valor inteiro digitado foi {numero} e o real foi {numero2}')