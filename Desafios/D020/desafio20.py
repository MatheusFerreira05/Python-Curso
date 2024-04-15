from random import shuffle

nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')

nomes = [nome1,nome2,nome3,nome4]

shuffle(nomes)

print('A sequencia das apresentações será: {}'.format(nomes))