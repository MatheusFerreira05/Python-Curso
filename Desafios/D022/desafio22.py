nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em Maíscula: {}'.format(nome.upper()))
print('Seu nome em Minúscula: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))