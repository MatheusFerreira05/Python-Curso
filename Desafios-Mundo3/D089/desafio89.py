alunos = []

while True:
    nome = input('Digite o nome do Aluno: ')
    nota1 = float(input(f'Digite a primeira nota do(a) Aluno(a) {nome}: '))
    nota2 = float(input(f'Digite a segunda nota do(a) Aluno(a) {nome}: '))
    media = (nota1 + nota2)/2
    notas = [nome, nota1,nota2, media]
    alunos.append(notas[:])

    continuar = input('Você quer continuar? [S/N]: ').upper()
    if continuar == 'N':
        break

print('-='*30)
print(f'{"nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, aluno in enumerate(alunos):
    print(f'{i+1:<4}{aluno[0]:<10}{aluno[3]:>8.1f}')
print('-'*25)

mostrarNotas = int(input('Mostrar notas de qual aluno? (Digite o número do aluno, 999 interrompe): '))

while mostrarNotas != 999:
    if mostrarNotas <= len(alunos):
        print(f'Notas de {alunos[mostrarNotas-1][0]} são {alunos[mostrarNotas-1][1],alunos[mostrarNotas-1][2]}')
        print('-'*25)
    else:
        print('Nº do Aluno inválido')
    mostrarNotas = int(input('Mostrar notas de qual aluno? (Digite o número do aluno, 999 interrompe): '))
print('*'*25)
print('FINALIZANDO...')