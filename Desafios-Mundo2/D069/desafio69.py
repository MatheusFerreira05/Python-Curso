continuar = 'S'
contadorMaior18 = 0
contadorHomem = 0
contadorMulherMenos20 = 0
while continuar == 'S':
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()
    print('-'*25)

    if idade > 18:
        contadorMaior18 += 1
    if sexo == 'M':
        contadorHomem += 1
    if sexo == 'F' and idade < 20:
        contadorMulherMenos20 += 1
    
    continuar = input('Quer continuar? ').upper()

print(f'Foram cadastradas {contadorMaior18} pessoas maior que 18 anos')
print(f'Foram cadastradas {contadorHomem} Homens')
print(f'Foram cadastradas {contadorMulherMenos20} mulheres menores que 20 anos')    
