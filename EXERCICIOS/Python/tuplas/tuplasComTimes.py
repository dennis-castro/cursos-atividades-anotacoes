from operator import index
from re import T
from uteis.str import titulo


titulo('Tabela do Brasileirão 2021')
lista = (
    'corinthians', 'palmeiras', 'santos', 'gremio',
    'cruzeiro', 'flamengo', 'vasco', 'chapecoense',
    'atletico', 'botafogo', 'atletico-pr', 'bahia',
    'sao paulo', 'fluminense', 'sport', 'vitoria',
    'coritiba', 'avai', 'ponte preta', 'atletico-go'
)
listaOrdemAlpha = sorted(lista)
for t in listaOrdemAlpha:
    print(t)

print()
print('*Os 5 primeiros colocados do brasileirão:')
for c in range(0, 5):
    print(f'{c+1} - {lista[c]}')
print()
print('*Times na zona de rebaixamento:')
for c in range(0, 4):
    print(f'{c+17} - {lista[c+16]}')
print()

while True:
    try:
        t = str(input('Escreva o nome time, para ver sua colocação: '))
        if t == '':
            print('O usuario nao informou nenhum time...')
            break
        print(f'{t} esta na {lista.index(t)+1}* colocação.')
        break
    except:
        print('Time não encontrado. Tente novamente...')
