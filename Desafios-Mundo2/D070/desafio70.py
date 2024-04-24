continuar = 'S'
total = 0
produtosMais1000 = 0
maisBarato = float('inf')
nomeMaisBarato = ''
while continuar == 'S':
    print('-'*25)
    print('Loja do Matheus')
    print('-'*25)
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    total += preco

    if total != 0:
        if preco > 1000:
            produtosMais1000 += 1
        if maisBarato > preco:
            maisBarato = preco
            nomeMaisBarato = produto
    else:
        maisBarato = preco
        nomeMaisBarato = produto
    continuar = input('Quer continuar? [S/N] ').upper()

print('--------- FIM DO PROGRAMA -----------')
print(f'O total da compra foi R${total}')
print(f'Temos {produtosMais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMaisBarato} que custa R${maisBarato}')