from datetime import date
hoje = date.today().year

pessoas = {}
c = 1
while True:
    #Nome
    pessoas[f'Nome {c}'] = input('Nome: ')
    #Data Nascimento
    dataNascimento = int(input('Ano de Nascimento: '))
    pessoas[f'Idade{c}'] = hoje - dataNascimento
    #Carteira de Trabalho
    carteira = int(input('Carteira de trabalho (0 não tem): '))
    if carteira != 0:
        pessoas[f'Carteira{c}'] = carteira
        #Ano Contratação
        pessoas[f'Ano Contratação{c}'] = int(input('Digite o ano de contratação: '))
        #Salário
        pessoas[f'Salário{c}'] = float(input('Digite o salário: '))
        #Aposentadoria
        aposentadoria = 35 - (hoje - pessoas[f'Ano Contratação{c}'])

        if aposentadoria == 0 or aposentadoria < 0:
            pessoas[f'Aposentadoria{c}']  = 'Aposentado'
        else:
            pessoas[f'Aposentadoria{c}']  = aposentadoria + pessoas[f'Idade{c}']

    continuar = int(input('DIGITE 999 PARA TERMINAR: '))

    if continuar == 999:
        break
    c += 1
print('='*40)
for i, p in pessoas.items():
    print(f'PESSOA {i}')
    print(f' - {i} tem o valor {p}')
    print('='*40)