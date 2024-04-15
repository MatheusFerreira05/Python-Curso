km = int(input('Digite a velocidade do carro: '))

if km > 80:
    kmMais = km-80
    multa = 7 * kmMais
    print('Você ultrapassou {}km e sua multa é de R$ {}'.format(kmMais,multa))
else:
    print('Siga em frente sua velocidade está dentro do permitido! ')