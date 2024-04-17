msg = input('Digite algo: ')

print('O tipo primitivo é: {}'.format(type(msg)))
print('Só tem espaços? {}'.format(msg.isspace()))
print('É um numero? {}'.format(msg.isnumeric()))
print('É alfabético? {}'.format(msg.isalpha()))
print('É alfanumerico? {}'.format(msg.isalnum()))
print('Está em maiúscula? {}'.format(msg.isupper()))
print('Está em minúscula? {}'.format(msg.islower()))