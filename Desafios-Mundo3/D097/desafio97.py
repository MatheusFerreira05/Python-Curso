def escreva(t):
    tamanho = len(t)+4
    print('~'*tamanho)
    print(f'  {t}')
    print('~'*tamanho)

texto = input('Escreva uma frase ')

escreva(texto)