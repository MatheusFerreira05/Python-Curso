frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O iverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Então {} é um Palíndromo'.format(frase))
else:
    print('Então {} não é um Palíndromo'.format(frase))