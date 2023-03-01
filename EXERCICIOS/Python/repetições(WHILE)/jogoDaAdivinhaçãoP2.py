
from random import randint
print('Ola!! eu sou seu COMPUTADOR, vamos jogar? \ntente adivinhar em qual numero estou pensando entre 1 a 10? ')
computador = randint(1,10)
verdadeiro = False
contador = 1
while not verdadeiro:
    jogador = int(input('Qual é sua jogada: '))
    contador += 1
    if jogador == computador:
        verdadeiro = True
    else:
        if jogador < computador:
            print('MAIS... tente novamente!')
        else:
            print('MENOS... tente novamente!')
    print('=-'*20)
print('PARABENS!!! voce acertou com {} tentativas'.format(contador))
