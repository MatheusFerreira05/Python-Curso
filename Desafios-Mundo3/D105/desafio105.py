def notas(* notas,sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    resumo = {}
    qtd = maior = media = soma = 0
    menor = 10
    
    qtd = len(notas)
    for nota in notas:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
        soma += nota
    media = soma / qtd

    if media > 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    resumo['total'] = qtd
    resumo['maior'] = maior
    resumo['menor'] = menor
    resumo['media'] = media
    if sit == True:
        resumo['situação'] = situacao

    print(resumo)

#notas(6,2,3,sit=True)
help(notas)