num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
num4 = int(input('Digite o 4º número: '))

tupla = (num1, num2, num3, num4)

numeros9 = tupla.count(9)
if 3 in tupla:
    numero3 = tupla.index(3)
else:
    numero3 = -1

print('-=' * 25)
print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu {numeros9} vezes')
if numero3 != -1:
    print(f'O número 3 apareceu pela primeira vez na {numero3 + 1}° posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
