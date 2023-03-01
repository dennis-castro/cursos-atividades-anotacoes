divisiveis = 0
num =  int(input('Digite um numero inteiro: '))
for c in range ( 1, num + 1):
    if num % c == 0:
        print('\033[32m',end='')
        divisiveis =  divisiveis + 1
    else:
        print('\033[31m',end='')
    print(c,end=', ')
print('\n\033[mO numero \033[34m{}\033[m foi divisivel \033[34m{}\033[m vezes.'.format(num, divisiveis))

if divisiveis == 2:
    print('Por isso ele é primo!!')
else:
    print('Por isso ele NÃO é primo!!')