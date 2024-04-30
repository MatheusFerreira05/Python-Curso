def fatorial(num,show=False):
    '''
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    '''

    c = num-1
    if show == False:
        while c > 1:
            num *= c
            c-=1
    else:
        print(f'{num} x',end=' ')
        while c >= 1:
            if c == 1:
                print(f'{c}',end=' = ')
            else:
                print(f'{c} x',end=' ')
            num *= c
            c-=1
    print(num)

fatorial(5,True)