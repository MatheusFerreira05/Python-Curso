print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print('O triângulo formado será Equilátero com todos os lado iguais!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo formado será Isóceles, tendo dois lados iguais!')
    else:
        print('O triângulo formado será Escaleno, tendo todos os lados diferentes!')
else:
    print('Os segmentos acima NÃO podem formar um TRIÂNGULO')