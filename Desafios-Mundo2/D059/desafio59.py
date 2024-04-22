num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

opcao = 0

while opcao != 5:
    print('-='*21)
    print('Escolha uma opção:')
    print('''
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair
    ''')
    print('-='*21)
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('{} + {} = {}'.format(num1,num2,num1 + num2))
    elif opcao == 2:
        print('{} x {} = {}'.format(num1,num2,num1*num2))
    elif opcao == 3:
        if num1 > num2:
            print('O primeiro número é maior que o Segundo')
        elif num2 > num1:
            print('O segundo número é maior que o Primeiro')
        elif num1 == num2:
            print('Os dois números são iguais')
    elif opcao == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))