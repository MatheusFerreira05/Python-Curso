
def ajuda(c):
    help(c)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print(msg)
    print('~'*tam)

comando = ''
while True:
    titulo('  SISTEMA DE AJUDA PyHELP')
    comando = input('Função ou Biblioteca > ' )
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo('  Até Logo!')