times = ('BRAGANTINO','FLAMENGO','BOTAFOGO','ATHLETICO PR','GRÊMIO','INTERNACIONAL','ATLETICO MG','FORTALEZA','BAHIA','FLUMINENSE','PALMEIRAS','CRUZEIRO','JUVENTUDE','SÃO PAULO','VASCO','CRICIÚMA', 'VITÓRIA','CORINTHIANS','ATLETICO GO', 'CUIABA')

primeiros = times[0:5]
ultimos = times[-4:]
ordemAlfa = sorted(times)
posicaoFluminense = times.index('FLUMINENSE')

print('-='*21)
print('Analisando a tabela do Campeonato...')
print('-='*21)

print(f'Os 5 primeiros colocados são: {primeiros}')
print('-='*21)
print(f'Os 5 últimos colocador são: {ultimos}')
print('-='*21)
print(f'Os times em odem alfabética fica: {ordemAlfa}')
print('-='*21)
print(f'O fluminense está na {posicaoFluminense+1}° posição')
print('-='*21)