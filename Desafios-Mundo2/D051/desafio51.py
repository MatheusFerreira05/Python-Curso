print('*='*21)
termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
print('*='*21)
decimo = termo + (10-1) * razao
for x in range(termo,decimo + razao,razao):
    print(x)
    