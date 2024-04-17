somaIdade = 0
mediaIdade = 0
maiorHomem = 0
nomeVelho = ''
totalMulher = 0

for pessoa in range(1,5):
    print('Pessoa {}'.format(pessoa))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorHomem:
        maiorHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totalMulher += 1
mediaIdade = somaIdade / 4
print('A média de idade dessas pessoas é de {} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maiorHomem,nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totalMulher))