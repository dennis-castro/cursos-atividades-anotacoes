import random
import time
itens =  ('PEDRA','PAPEL','TESOURA')
computador =  random.randint(0, 2)
print('''Suas opções são:
[0] pedra
[1] papel
[2] tesoura''')
jogador = int(input('Qual é sua jogada? '))
print()
print('JOOOOOO...')
time.sleep(1)
print('KENNN...')
time.sleep(1)
print('PO!!!!!!!')
time.sleep(1)

print('\033[1;31m O computador jogou {} \033[m'.format(itens[computador]))
print('\033[1;32m O jogador jogou {} \033[m '.format(itens[jogador]))
print('=-'*20)

if computador == 0: # jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
    else:
        print('Opção invalida')


elif computador == 1: # jogou PAPEL
    if jogador ==0:
        print('JOGADOR PERDEU')
    elif jogador ==1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('Opção invalida')

elif computador ==2: # jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador ==1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opção invalida')






