from random import randint

lista = []
print('='*30)
quantJogo = int(input('\033[31mQuantos jogos deseja fazer: \033[m'))
print('='*30)
for qj in range(1, quantJogo+1):
    lista.clear()
    for j in range(1, 7):
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
    lista.sort()
    print(f'JOGO NUMERO-{qj}')
    print(f'\033[32m{lista}\033[m')
    print('='*30)
