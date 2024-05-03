from uteis.menu import *
from uteis.arquivo import *
from time import sleep

arq = 'sistemacadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu(["Ver pessoas cadastradas","Cadastrar nova pessoa","Sair do Sistema"])
    if opcao == 1:
        linha()
        cabecalho('PESSOAS CADASTRADAS',3)
        lerArquivo(arq)
        linha()
    elif opcao == 2:
        linha()
        cabecalho('NOVO CADASTRO',3)
        nome = input('Nome: ')
        idade = input('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        linha()
        cabecalho('Saindo do Sistema... Até logo!')
        break
    elif opcao < 1 or opcao > 3:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
