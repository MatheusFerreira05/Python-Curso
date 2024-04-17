altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

imc = peso/ (altura * altura)

if imc <= 18.5:
    print('ABAIXO DO PESO, imc = {:.2f}'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('PESO IDEAL imc = {:.2f}'.format(imc))
elif imc > 25 and imc <= 30:
    print('SOBREPESO imc = {:.2f}'.format(imc))
elif imc > 30 and imc <= 40:
    print('OBESIDADE imc = {:.2f}'.format(imc))
else:
    print('OBESIDADE MÓRBIDA imc = {}'.format(imc))