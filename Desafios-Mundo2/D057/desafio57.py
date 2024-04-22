sexo = input('Digite o sexo da pessoa (M ou F): ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo da pessoa (M ou F): ').upper()
print('Certo o sexo é: {}'.format(sexo))