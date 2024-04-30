def leiaInt(numero):
    while numero.isnumeric() != True:
        print('\033[0;31mERRO! Digite um número inteiro válido\033[m')
        numero = input('Digita ai: ')
    else: 
        return numero
        
numero = leiaInt(input('Digita ai: '))
print(f'Você digitou o número {numero}')

