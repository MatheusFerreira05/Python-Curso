from datetime import date
hoje = date.today().year

nascimento = int(input('Qual é seu ano de nascimento? '))

idade = hoje - nascimento

if idade < 18:
    print('Você terá que se alistar no exército daqui {} ano(s)'.format(18-idade))
elif idade == 18:
    print('Você tem que se alistar para o exército nesse ano!')
else:
    print('Você já passou do tempo de se alistar para o exército já fazem {} ano(s)'.format(idade-18))