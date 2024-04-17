num = int(input('Digite um número: '))
t = 0
for x in range(1, num +1):
    if num % x == 0:
        print('\033[33m',end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(num), end='')

print('\n\033[mO número {} foi divisivel {} vezes'.format(num,t))
if t == 2:
    print('Então ele é primo!')
else:
    print('Então ele não é primo')