while True:
    print('-'*35)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)
    cont = 1
    if tabuada > 0:
        while cont <= 10:
            print(f'{tabuada} x {cont} = {cont * tabuada}')
            cont += 1
    else:
        break
print('Programa tabuada encerrado!')
    
