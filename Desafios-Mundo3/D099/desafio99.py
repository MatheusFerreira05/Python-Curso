from time import sleep
def maior(*num):
    m = 0
    lista = []
    if num != '':
        for numero in num:
            lista.append(numero)
            if m == 0:
                m = numero
            elif numero > m:
                m = numero  
        print('-='*30)
        print('Analisando os valores passados...')
        for numero in num:
            print(numero,end=' ')
            sleep(0.5)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {m}')
    else:
        print('-='*30)
        print('Analisando os valores passados...')
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {m}')
    
maior(6,5,9,3)
maior(4,7,0)
maior(2)
maior()

