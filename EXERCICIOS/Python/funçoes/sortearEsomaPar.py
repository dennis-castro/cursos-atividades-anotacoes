from random import randint
from time import sleep


def sortear():
    print('-'*50)
    print('Sorteando os numeros: ', end='')
    for n in range(1, 6):
        n = randint(1, 10)
        numSort.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print()
    print('-'*50)


def somaPar():
    soma = 0
    print('-'*50)
    print('Os numeros PARES encontrados foi: ', end='')
    for n in numSort:
        if n % 2 == 0:
            soma += n
            print(f'{n}', end=' ')
    print()
    print(f'A soma de todos os numeros pares foi de: {soma}')
    print('-'*50)


numSort = []
sortear()
somaPar()
