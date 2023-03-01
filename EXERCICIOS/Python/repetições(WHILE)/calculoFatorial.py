f = 1
num = int(input('Digite um numero: '))
print('Calculando {}! = '.format(num), end='')
for c in range(num, 0, -1):
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '=', end='')
    f = f*c
    c = c-1
print(' {}'.format(f),end='')