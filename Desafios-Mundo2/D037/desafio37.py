num = int(input('Digite um número inteiro: '))
print('''Escolha qual a base você quer converter:
      [1] Binário
      [2] Octal
      [3] Hexadecimal
      ''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido em binário é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, tente novamente.')