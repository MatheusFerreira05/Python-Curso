lista = []
idades = []
somaIdades = 0
mediaIdades = 0
qtdMulheres = []
acimaMedia = []
while True:
    pessoa = {}
    nome = input('Nome: ')
    sexo = input('Sexo [M/F]: ').upper()
    idade = int(input('Idade: '))

    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade

    lista.append(pessoa.copy())

    if sexo == 'F':
        qtdMulheres.append(nome)

    continuar = int(input('Quer continuar? (999 para parar: )'))

    if continuar == 999:
        break

for c in lista:
    idade = (c['idade'])
    somaIdades += idade
mediaIdades = somaIdades / len(lista)

for c in lista:
    idade = (c['idade'])
    nome = (c['nome'])
    sexo = (c['sexo'])

    if idade > mediaIdades:
        pessoaAcimaMedia = {}
        pessoaAcimaMedia['nome'] = nome
        pessoaAcimaMedia['idade'] = idade
        pessoaAcimaMedia['sexo'] = sexo
        acimaMedia.append(pessoaAcimaMedia)

print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.' )
print(f'- A média de idade é de {mediaIdades} anos.')
if qtdMulheres != []:
    print(f'As mulheres cadastradas foram: ',end='')
    for mulher in qtdMulheres:
        print(mulher)
        print(end='')
else:
    print('Não foram cadastradas mulheres!')
print('- Lista de pessoas que estão acima da média: ')
for p in acimaMedia:
    print(p)
