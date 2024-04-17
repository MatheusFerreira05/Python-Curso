num = int(input('Digite um valor para saber sua tabuada: '))

for x in range(1,11):
    print('{} x {} = {}'.format(num,x,(num*x)))