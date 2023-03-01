from time import sleep
from random import randint
cont= 0
parImpar = ' '
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1,10)
    total = jogador + computador
    parImpar = str(input('PAR ou IMPAR [P/I]: ')).strip().upper()[0]
    while parImpar not in 'PI':
        parImpar = str(input('PAR ou IMPAR [P/I]: ')).strip().upper()[0]
    print(f'Voce Jogou {jogador} e o computador jogou {computador} total de  {total}')
    if parImpar == 'P':
        if total % 2 == 0:
            print('Deu PAR voce ganhou!!')
            vitorias += 1
        else:
            print('Voce perdeu!!')
            break
    elif parImpar == 'I':
        if total % 2 == 1:
            print('Deu IMPAR voce ganhou!!')
            vitorias += 1
        else:
            print('Voce perdeu!!')
            break
    print('Vamos jogar novamente...')
    print('-='*30)
    sleep(2)
print(f'GAME OVER!!! voce venceu {vitorias} vitorias. ')