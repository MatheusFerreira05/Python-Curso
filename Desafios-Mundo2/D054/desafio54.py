from datetime import date

ano = date.today().year
totalMaior = 0
totalMenor = 0
for pessoa in range (1,8):
    nascimento = int(input('Em qual ano a pessoa {} nasceu? '.format(pessoa)))
    idade = ano - nascimento
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print('=-*'*20)
print('Analisando...')
print('=-*'*20)

print('Temos {} pessoas maiores de idade'.format(totalMaior))
print('Temos {} pessoas menores de idade'.format(totalMenor))