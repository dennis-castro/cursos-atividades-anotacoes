from ntpath import join
from operator import itemgetter
from random import randint
from time import sleep


jogo = {
    'JOGADOR(A)':randint(1,6),
    'JOGADOR(B)':randint(1,6),
    'JOGADOR(C)':randint(1,6),
    'JOGADOR(D)':randint(1,6),
    'JOGADOR(E)':randint(1,6) 
}
rank = {}

print(f'{"Valores sorteados":.^40}')
sleep(0.5)
for k, v in jogo.items():
    sleep(0.5)
    print(f'{k} numero sorteado:  {v}')
print('.'*40)

rank = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print (f'{"=RANKING DOS JOGADORES=":^40}')
for k, v in enumerate(rank):
    print(f'{k+1}-{v[0]}: {v[1]}')

