largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

parede = largura*altura

tinta = parede/2

print('Você precisará de {} litros de tinta para uma parede com {} metros quadrados'.format(tinta,parede))