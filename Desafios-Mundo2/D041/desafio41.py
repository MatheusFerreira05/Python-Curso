from datetime import date
hoje = date.today().year

ano = int(input('Digite o ano de nascimento do atleta: '))

idade = hoje - ano

if idade <= 9:
    print('{} anos, CATEGORIA MIRIM'.format(idade))
elif idade <= 14:
    print('{} anos, CATEGORIA INFANTIL'.format(idade))
elif idade <= 19:
    print('{} anos, CATEGORIA JUNIOR'.format(idade))
elif idade <= 20:
    print('{} anos, CATEGORIA SÊNIOR'.format(idade))
else:
    print('{} anos, CATEGORIA MASTER'.format(idade))
