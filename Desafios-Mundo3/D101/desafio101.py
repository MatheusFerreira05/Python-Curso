def voto(data):
    from datetime import date
    hoje = date.today().year
    idade = hoje - data

    if idade >= 65:
        print(f'Com {idade} anos o voto é opcional!')
    elif idade > 18 and idade < 65:
        print(f'Com {idade} anos, o voto é obrigatório!')
    elif idade < 18:
        print(f'Com {idade} anos, não Vota')



nasc = int(input('Em que ano você nasceu? '))

voto(nasc)