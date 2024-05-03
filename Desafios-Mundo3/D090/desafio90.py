aluno = {}

aluno['Nome'] = input('Digite o nome do aluno: ')
media = aluno['Média'] = float(input('Digite a média do aluno: '))

if media >= 7:
    aluno['Situação'] = "Aprovado"
else:
    aluno['Situação'] = "Reprovado"

for k,v in aluno.items():
    print(f'{k} é igual a {v}')