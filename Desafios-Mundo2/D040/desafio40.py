nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5.0:
    print('=-'*21)
    print('Média {} REPROVADO'.format(media))
    print('=-'*21)
elif media >= 5.0 and media < 6.9:
    print('=-'*21)
    print('Média {} RECUPERAÇÃO'.format(media))
    print('=-'*21)
else:
    print('=-'*21)
    print('Média {} APROVADO'.format(media))
    print('=-'*21)