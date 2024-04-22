num = int(input('Digite um número: '))
c = num
fatorial = 1

print('Calculando {}! = '.format(num),end='')

while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ')
    fatorial *= c
    c -= 1
print('{}'.format(fatorial))